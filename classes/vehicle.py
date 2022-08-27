class Vehicle:
    def __init__(
        self,
        vehicle_id,
        max_speed_in_kmh,
        max_load_in_kg,
        actual_load_in_kg,
        in_transit,
        available_in,
    ):
        self.__vehicle_id = vehicle_id
        self.__max_speed_in_kmh = max_speed_in_kmh
        self.__max_load_in_kg = max_load_in_kg
        self.__actual_load_in_kg = actual_load_in_kg
        self.__in_transit = in_transit
        self.__available_in = available_in

    def get_vehicle_dict(self):
        return {
            "vehicle_id": self.__vehicle_id,
            "max_speed_in_kmh": self.__max_speed_in_kmh,
            "max_load_in_kg": self.__max_load_in_kg,
            "actual_load_in_kg": self.__actual_load_in_kg,
            "in_transit": self.__in_transit,
            "available_in": self.__available_in,
        }

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_max_speed_in_kmh(self):
        return self.__max_speed_in_kmh

    def get_max_load_in_kg(self):
        return self.__max_load_in_kg

    def get_actual_load_in_kg(self):
        return self.__actual_load_in_kg

    def get_in_transit(self):
        return self.__in_transit

    def get_available_in(self):
        return self.__available_in
