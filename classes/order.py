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
                {
                    "pkg_id": i.get("package").get_pkg_id(),
                    "distance_in_km": i.get("distance_in_km"),
                    "offer_code": i.get("offer").get_offer_code(),
                }
                for i in self.__delivery_info
            ],
        }

    def get_order_code(self):
        return self.__order_code

    def get_no_of_packges(self):
        return int(self.__no_of_packges)

    def get_delivery_info(self):
        return self.__delivery_info
