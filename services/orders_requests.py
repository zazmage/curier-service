import json

from classes.order import Order


def load_orders():
    try:
        with open("./databases/orders.json", "r") as file:
            orders = json.loads(file.read())
            orders_list = [
                Order(
                    i.get("order_code"),
                    i.get("no_of_packges"),
                    i.get("packages"),
                )
                for i in orders
            ]
            return orders_list
    except:
        return []


def save_order(order):
    try:
        with open("./databases/orders.json", "r+") as file:
            orders = json.loads(file.read())
            orders.append(order)
            file.seek(0)
            json.dump(orders, file, indent=2)
    except:
        print("Something went wrong...")
