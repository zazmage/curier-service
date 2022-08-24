from classes.offers_list import Offers_list
from classes.packages_list import Packages_list
from services.offers_requests import load_offers
from services.orders_requests import load_orders
from services.packages_requests import load_packages


class Order:
    def __init__(
        self,
        pkg_id,
        no_of_packges,
        distance_in_km,
        offer_code,
    ) -> None:
        self.__pkg_id = pkg_id
        self.__no_of_packges = no_of_packges
        self.__distance_in_km = distance_in_km
        self.__offer_code = offer_code

    def get_order_dict(self):
        return {
            "pkg_id": self.__pkg_id,
            "no_of_packges": self.__no_of_packges,
            "distance_in_km": self.__distance_in_km,
            "offer_code": self.__offer_code,
        }

    def get_package(self):
        packages = Packages_list()
        return next(
            (
                i
                for i in packages.get_packages()
                if i.get_pkg_id() == self.__pkg_id
            ),
            None,
        )

    def get_pkg_id(self):
        return self.__pkg_id

    def get_no_of_packges(self):
        return int(self.__no_of_packges)

    def get_distance_in_km(self):
        return int(self.__distance_in_km)

    def get_offer(self):
        offers = Offers_list()
        return next(
            (
                i
                for i in offers.get_offers()
                if i.get_offer_code() == self.__offer_code
            ),
            None,
        )

    def get_offer_code(self):
        return self.__offer_code
