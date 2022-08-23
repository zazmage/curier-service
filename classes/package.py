class Package:
    def __init__(self, pkg_id, base_delivery_cost, pkg_weight_in_kg):
        self.__pkg_id = pkg_id
        self.__base_delivery_cost = base_delivery_cost
        self.__pkg_weight_in_kg = pkg_weight_in_kg

    def get_pkg_id(self):
        return self.__pkg_id

    def get_base_delivery_cost(self):
        return self.__base_delivery_cost

    def get_pkg_weight_in_kg(self):
        return self.__pkg_weight_in_kg
