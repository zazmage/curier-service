class Vehicle:
    def __init__(
        self,
        vehicle_id,
        max_speed_in_kmh,
        max_load_in_kg,
        actual_load_in_kg,
        available_in_h,
        deliveries,
    ):
        self.__vehicle_id = vehicle_id
        self.__max_speed_in_kmh = max_speed_in_kmh
        self.__max_load_in_kg = max_load_in_kg
        self.__actual_load_in_kg = actual_load_in_kg
        self.__available_in_h = available_in_h
        self.__deliveries = deliveries

    def get_vehicle_dict(self):
        return {
            "vehicle_id": self.__vehicle_id,
            "max_speed_in_kmh": self.__max_speed_in_kmh,
            "max_load_in_kg": self.__max_load_in_kg,
            "actual_load_in_kg": self.__actual_load_in_kg,
            "available_in_h": self.__available_in_h,
            "deliveries": self.__deliveries,
        }

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_max_speed_in_kmh(self):
        return self.__max_speed_in_kmh

    def get_max_load_in_kg(self):
        return self.__max_load_in_kg

    def get_actual_load_in_kg(self):
        return self.__actual_load_in_kg

    def get_available_in_h(
        self,
    ):
        return self.__available_in_h

    def get_deliveries(self):
        return self.__deliveries

    def set_actual_load_in_kg(self, actual_load_in_kg):
        self.__actual_load_in_kg = actual_load_in_kg

    def set_available_in_h(self, available_in_h):
        self.__available_in_h = available_in_h

    def set_deliveries(self, deliveries):
        self.__deliveries.append(deliveries)
