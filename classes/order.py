def new_order_code(orders):
    orders = [i.get_order_code() for i in orders]
    max_order = 0
    for i in orders:
        order_code_number = int("".join([j for j in [*i] if j.isnumeric()]))
        if max_order < order_code_number:
            max_order = order_code_number

    return f"ORD{max_order + 1}"


class Order:
    def __init__(self, order_code, no_of_packges, delivery_info) -> None:
        self.__order_code = order_code
        self.__no_of_packges = no_of_packges
        self.__delivery_info = delivery_info

    def get_order_dict(self):
        return {
            "order_code": self.__order_code,
            "no_of_packges": self.__no_of_packges,
            "delivery_info": [
                i.get_delivery_info_dict() for i in self.__delivery_info
            ],
        }

    def get_order_code(self):
        return self.__order_code

    def get_no_of_packges(self):
        return int(self.__no_of_packges)

    def get_delivery_info(self):
        return self.__delivery_info
