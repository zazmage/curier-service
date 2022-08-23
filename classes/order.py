from services.offers_requests import load_offers
from services.orders_requests import load_orders
from services.packages_requests import load_packages


class Order:
    def __init__(
        self,
        package,
        no_of_packges,
        distance_in_km,
        offer,
    ) -> None:
        self.__package = package
        self.__no_of_packges = no_of_packges
        self.__distance_in_km = distance_in_km
        self.__offer = offer

    def get_order_dict(self):
        return {
            "pkg_id": self.__package,
            "no_of_packges": self.__no_of_packges,
            "distance_in_km": self.__distance_in_km,
            "offer_code": self.__offer,
        }

    def get_package(self):
        packages = load_packages()
        return next(
            (i for i in packages if i.get("pkg_id") == self.__package), None
        )

    def get_no_of_packges(self):
        return self.__no_of_packges

    def get_distance_in_km(self):
        return self.__distance_in_km

    def get_offer(self):
        offers = load_offers()
        return next(
            (i for i in offers if i.get("pkg_id") == self.__offer), None
        )
