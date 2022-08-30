from commands.command_line import expect_input, no_results, separator
from services.delivery_requests import save_delivery


def create_delivery_queue(orders):
    queue = []
    for i in orders:
        for j in i.get_delivery_info():
            queue.append(
                {
                    "order_code": i.get_order_code(),
                    "pkg_id": j.get("package").get_pkg_id(),
                    "pkg_weight_in_kg": j.get(
                        "package"
                    ).get_pkg_weight_in_kg(),
                    "distance_in_km": j.get("distance_in_km"),
                }
            )
    queue.sort(key=lambda x: x.get("pkg_weight_in_kg"), reverse=True)
    return queue


def show_deliveries(deliveries):
    separator()
    if deliveries:
        for i in deliveries:
            print("Vehicle ID: ", i.get_vehicle_id())
            print("Available in h: ", i.get_available_in_h())
            print("Deliveries: ")
            for j in i.get_deliveries():
                print(
                    "---> Travel time (h): ",
                    j.get("travel_time_in_h"),
                )
                print(
                    "---> Delivery info: ",
                )
                for k in j.get("delivery_info"):
                    print(
                        "-------> Order code: ",
                        k.get("order_code"),
                    )
                    print(
                        "-------> Package ID: ",
                        k.get("pkg_id"),
                    )
                    print(
                        "-------> Package weight (kg): ",
                        k.get("pkg_weight_in_kg"),
                    )
                    print(
                        "-------> Distance (km): ",
                        k.get("distance_in_km"),
                    )
                    print("--------")
                print("----")
        separator()
    else:
        no_results()
    expect_input()


def show_assigned_deliveries(vehicles):
    separator()
    for i in vehicles:
        print("Vehicle ID: ", i.get_vehicle_id())
        print("Available in h: ", i.get_available_in_h())
        print("Deliveries: ")
        for j in i.get_deliveries():
            print(
                "---> Travel time (h): ",
                j.get("travel_time_in_h"),
            )
            print(
                "---> Delivery info: ",
            )
            for k in j.get("delivery_info"):
                print(
                    "-------> Order code: ",
                    k.get("order_code"),
                )
                print(
                    "-------> Package ID: ",
                    k.get("pkg_id"),
                )
                print(
                    "-------> Package weight (kg): ",
                    k.get("pkg_weight_in_kg"),
                )
                print(
                    "-------> Distance (km): ",
                    k.get("distance_in_km"),
                )
                print("--------")
            print("----")
    separator()
    expect_input()


def assign_deliveries(orders, vehicles):
    queue = create_delivery_queue(orders)
    while queue:
        vehicles.sort(key=lambda x: x.get_available_in_h())
        assigned_vehicle = vehicles[0]
        delivery_info = []
        travel_time = 0
        for i in queue:
            if (
                i.get("pkg_weight_in_kg")
                + assigned_vehicle.get_actual_load_in_kg()
                <= assigned_vehicle.get_max_load_in_kg()
            ):
                new_travel_time = round(
                    i.get("distance_in_km")
                    / assigned_vehicle.get_max_speed_in_kmh()
                    * 2,
                    2,
                )
                if travel_time < new_travel_time:
                    travel_time = new_travel_time

                assigned_vehicle.set_actual_load_in_kg(
                    round(
                        assigned_vehicle.get_actual_load_in_kg()
                        + i.get("pkg_weight_in_kg"),
                        2,
                    )
                )
                delivery_info.append(i)
                queue.remove(i)
        assigned_vehicle.set_available_in_h(
            assigned_vehicle.get_available_in_h() + travel_time
        )
        assigned_vehicle.set_deliveries(
            {"delivery_info": delivery_info, "travel_time_in_h": travel_time}
        )
        assigned_vehicle.set_actual_load_in_kg(0)
    for i in vehicles:
        save_delivery(
            i.get_vehicle_id(), i.get_available_in_h(), i.get_deliveries()
        )
    show_assigned_deliveries(vehicles)
