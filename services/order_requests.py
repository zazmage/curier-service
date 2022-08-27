import json

from classes.order import Order
from services.offer_requests import query_offer
from services.package_requests import query_package
from utils.utils import new_code


def load_orders():
    try:
        with open("./databases/orders.json", "r") as file:
            orders = json.loads(file.read())
            orders_list = [
                Order(
                    i.get("order_code"),
                    int(i.get("no_of_packges")),
                    [
                        {
                            "package": query_package(j.get("pkg_id")),
                            "distance_in_km": float(j.get("distance_in_km")),
                            "offer": query_offer(j.get("offer_code")),
                        }
                        for j in i.get("delivery_info")
                    ],
                )
                for i in orders
            ]
            return orders_list
    except:
        return []


def query_order(order_code):
    try:
        with open("./databases/orders.json", "r") as file:
            orders = json.loads(file.read())
            orders_list = [
                Order(
                    i.get("order_code"),
                    int(i.get("no_of_packges")),
                    [
                        {
                            "package": query_package(j.get("pkg_id")),
                            "distance_in_km": float(j.get("distance_in_km")),
                            "offer": query_offer(j.get("offer_code")),
                        }
                        for j in i.get("delivery_info")
                    ],
                )
                for i in orders
            ]
            order = next(
                (i for i in orders_list if i.get_order_code() == order_code),
                None,
            )
            return order
    except:
        return None


def save_order(no_of_packges, delivery_info):
    try:
        with open("./databases/orders.json", "r+") as file:
            orders = load_orders()
            order = {
                "order_code": new_code(
                    "ORD", [i.get_order_code() for i in orders]
                ),
                "no_of_packges": no_of_packges,
                "delivery_info": delivery_info,
            }
            orders = [i.get_order_dict() for i in orders]
            orders.append(order)
            file.seek(0)
            json.dump(orders, file, indent=2)
            print("Successfully created order...")
    except:
        print("Something went wrong...")
