import json
from classes.delivery_info import Delivery_info

from classes.order import Order, new_order_code
from services.offers_requests import query_offer
from services.packages_requests import query_package


def load_orders():
    try:
        with open("./databases/orders.json", "r") as file:
            orders = json.loads(file.read())
            orders_list = []
            for i in orders:

                delivery_info = []
                for j in i.get("delivery_info"):
                    delivery_info.append(
                        Delivery_info(
                            query_package(j.get("pkg_id")),
                            j.get("distance_in_km"),
                            query_offer(j.get("offer_code")),
                        )
                    )
                orders_list.append(
                    Order(
                        i.get("order_code"),
                        i.get("no_of_packges"),
                        delivery_info,
                    )
                )
            return orders_list
    except:
        return []


def query_order_code(order_code):
    try:
        with open("./databases/orders.json", "r") as file:
            orders = json.loads(file.read())
            orders_list = []
            for i in orders:
                delivery_info = []
                for j in i.get("delivery_info"):
                    delivery_info.append(
                        Delivery_info(
                            query_package(j.get("pkg_id")),
                            j.get("distance_in_km"),
                            query_offer(j.get("offer_code")),
                        )
                    )
                orders_list.append(
                    Order(
                        i.get("order_code"),
                        i.get("no_of_packges"),
                        delivery_info,
                    )
                )
            order = next(
                (i for i in orders_list if i.get_order_code() in order_code),
                None,
            )
            return order
    except:
        return []


def save_order(no_of_packges, delivery_info):
    # try:
    with open("./databases/orders.json", "r+") as file:
        orders = load_orders()
        order = Order(new_order_code(orders), no_of_packges, delivery_info)
        orders.append(order)
        orders_dict = [i.get_order_dict() for i in orders]
        file.seek(0)
        json.dump(orders_dict, file, indent=2)
        print("Successfully created order...")
    # except:
    #     print("Something went wrong...")
