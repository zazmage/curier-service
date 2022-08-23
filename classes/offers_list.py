from classes.offer import Offer
from services.offers_requests import load_offers


class Offers_list:
    def __init__(self) -> None:
        offers = load_offers()
        self.__offers = []
        for i in offers:
            self.__offers.append(
                Offer(
                    i.get("offer_Code"),
                    i.get("discount"),
                    i.get("distance_in_km"),
                    i.get("weight_in_kg"),
                )
            )

    def get_offers(self):
        return self.__offers
