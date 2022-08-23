from services.orders_requests import load_orders


class Orders_list:
    def __init__(self) -> None:
        self.__orders = load_orders()

    def get_orders(self):
        return self.__orders
