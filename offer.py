class offer:
    def __init__(self, offer_code, discount) -> None:
        self.__offer_code = offer_code
        self.__discount = discount

    def get_offer_code(self):
        return self.__offer_code

    def get_discount(self):
        return self.__discount
