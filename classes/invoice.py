class Invoice:
    def __init__(self, order):
        self.__order = order

        self.__discount = 0

        order_distance = order.get_delivery_info().get_distance_in_km()
        min_offer_distance = order.get_offer().get_min_distance_in_km()
        max_offer_distance = order.get_offer().get_max_distance_in_km()

        order_weight = order.get_package().get_pkg_weight_in_kg()
        min_offer_weight = order.get_offer().get_min_weight_in_kg()
        max_offer_weight = order.get_offer().get_max_weight_in_kg()

        discount_percentage = 0
        if min_offer_distance <= order_distance <= max_offer_distance:
            if min_offer_weight <= order_weight <= max_offer_weight:
                discount_percentage = order.get_offer().get_discount() / 100

        base_delivery_cost = order.get_package().get_base_delivery_cost()

        self.__delivery_cost = (
            base_delivery_cost + (order_weight * 10) + (order_distance * 5)
        )

        self.__discount = self.__delivery_cost * discount_percentage

        self.__total_cost = self.__delivery_cost - self.__discount

    def get_order(self):
        return self.__order

    def get_delivery_cost(self):
        return self.__delivery_cost

    def get_discount(self):
        return self.__discount

    def get_total_cost(self):
        return self.__total_cost
