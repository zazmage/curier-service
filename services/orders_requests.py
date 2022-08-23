import json


def load_orders():
    try:
        with open("./databases/orders.json", "r") as file:
            orders = json.loads(file.read())
            return orders
    except:
        return []
