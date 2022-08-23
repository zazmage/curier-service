from services.offers_requests import load_offers


class Offers_list:
    def __init__(self) -> None:
        self.__offers = load_offers()

    def get_offers(self):
        return self.__offers
