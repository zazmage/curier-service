class Delivery_info:
    def __init__(self, package, distance_in_km, offer):
        self.__package = package
        self.__distance_in_km = distance_in_km
        self.__offer = offer

    def get_delivery_info_dict(self):
        return {
            "package": self.__package,
            "distance_in_km": self.__distance_in_km,
            "offer_code": self.__offer,
        }

    def get_package(self):
        return self.__package

    def get_distance_in_km(self):
        return int(self.__distance_in_km)

    def get_offer(self):
        return self.__offer
