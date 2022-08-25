from services.packages_requests import query_package_id


class Delivery_info:
    def __init__(self, pkg_id, distance_in_km, offer_code):
        self.__package = query_package_id(pkg_id)
        self.__distance_in_km = distance_in_km
        self.__offer_code = offer_code

    def get_delivery_info_dict(self):
        return {
            "package": self.__package.get_pkg_id(),
            "distance_in_km": self.__distance_in_km,
            "offer_code": self.__offer_code,
        }

    def get_package(self):
        return self.__package

    def get_distance_in_km(self):
        return int(self.__distance_in_km)

    def get_offer_code(self):
        return int(self.__offer_code)
