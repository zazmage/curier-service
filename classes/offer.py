class Offer:
    def __init__(
        self, offer_code, discount, distance_in_km, weight_in_kg
    ) -> None:
        self.__offer_code = offer_code
        self.__discount = discount
        self.__distance_in_km = distance_in_km
        self.__weight_in_kg = weight_in_kg

    def get_offer_code(self):
        return self.__offer_code

    def get_discount(self):
        return self.__discount

    def get_distance_in_km(self):
        return self.__distance_in_km

    def get_weight_in_kg(self):
        return self.__weight_in_kg
