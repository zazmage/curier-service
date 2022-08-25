from classes.offers_list import Offers_list
from classes.packages_list import Packages_list
from services.offers_requests import load_offers
from services.orders_requests import load_orders
from services.packages_requests import load_packages


def new_order_code(orders):
    orders = load_orders()
    orders = [i.get("order_code") for i in orders]
    max_order = 0
    for i in orders:
        order_code_number = int("".join([j for j in [*i] if j.isnumeric()]))
        if max_order < order_code_number:
            max_order = order_code_number

    return f"ORD{max_order + 1}"


class Order:
    def __init__(self, no_of_packges, delivery_info) -> None:
        self.__order_code = new_order_code()
        self.__no_of_packges = no_of_packges
        self.__delivery_info = delivery_info

    def get_order_dict(self):
        return {
            "order_code": self.__order_code,
            "no_of_packges": self.__no_of_packges,
            "delivery_info": self.__delivery_info.get_delivery_info_dict(),
        }

    def get_order_code(self):
        return self.__order_code

    def get_no_of_packges(self):
        return int(self.__no_of_packges)

    def get_delivery_info(self):
        return self.__delivery_info
