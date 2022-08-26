class Delivery_info:
    def __init__(self, package, distance_in_km, offer):
        self.__package = package
        self.__distance_in_km = distance_in_km
        self.__offer = offer

    def get_delivery_info_dict(self):
        return {
            "pkg_id": self.__package.get_pkg_id(),
            "distance_in_km": self.__distance_in_km,
            "offer_code": self.__offer.get_offer_code(),
        }

    def get_package(self):
        return self.__package

    def get_distance_in_km(self):
        return int(self.__distance_in_km)

    def get_offer(self):
        return self.__offer
