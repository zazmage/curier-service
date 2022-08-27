from commands.command_line import (
    expect_input,
    guarantee_int,
    mid_sep,
    separator,
)
from services.order_requests import save_order


def show_orders(orders):
    separator()
    for i in orders:
        print("Order code: ", i.get_order_code())
        print("Number of packages: ", i.get_no_of_packges())
        print("Delivery info: ")
        for j in i.get_delivery_info():
            print(
                "---> Package ID: ",
                j.get("package").get_pkg_id(),
            )
            print(
                "---> Distance in km: ",
                j.get("distance_in_km"),
            )
            print("---> Offer code: ", j.get("offer").get_offer_code())
            print("-")
        mid_sep()
    separator()
    expect_input()


def create_order():
    no_of_packges = guarantee_int("Number of packages: ")
    delivery_info = []
    for i in range(1, no_of_packges + 1):
        pkg_id = input(f"Package {i} ID: ")
        distance_in_km = input(f"Package {i} distance in kilometers: ")
        offer_code = input(f"Package {i} Offer ID: ")
        delivery_info.append(
            {
                "pkg_id": pkg_id,
                "distance_in_km": distance_in_km,
                "offer_code": offer_code,
            }
        )
    save_order(no_of_packges, delivery_info)
