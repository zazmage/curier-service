import json


def load_orders():
    try:
        with open("./databases/orders.json", "r") as file:
            orders = json.loads(file.read())
            return orders
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
