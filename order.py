class order:
    def __init__(
        self,
        packages,
        distance_in_km,
        offer,
    ) -> None:
        self.__packages = packages
        self.__no_of_packges = len(packages)
        self.__distance_in_km = distance_in_km
        self.__offer = offer

    def get_packages(self):
        return self.__packages

    def get_no_of_packges(self):
        return self.__no_of_packges

    def get_distance_in_km(self):
        return self.__distance_in_km

    def get_offer(self):
        return self.__offer
