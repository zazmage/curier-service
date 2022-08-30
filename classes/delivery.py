class Delivery:
    def __init__(self, delivery_code, vehicle_id, available_in_h, deliveries):
        self.__delivery_code = delivery_code
        self.__vehicle_id = vehicle_id
        self.__available_in_h = available_in_h
        self.__deliveries = deliveries

    def get_delivery_dict(self):
        print(
            "dict: ",
            {
                "delivery_code": self.__delivery_code,
                "vehicle_id": self.__vehicle_id,
                "available_in_h": self.__available_in_h,
                "deliveries": [
                    {
                        "travel_time_in_h": i.get("travel_time_in_h"),
                        "delivery_info": [
                            {
                                "order_code": j.get("order_code"),
                                "pkg_id": j.get("pkg_id"),
                                "pkg_weight_in_kg": j.get("pkg_weight_in_kg"),
                                "distance_in_km": j.get("distance_in_km"),
                            }
                            for j in i.get("delivery_info")
                        ],
                    }
                    for i in self.__deliveries
                ],
            },
        )
        return {
            "delivery_code": self.__delivery_code,
            "vehicle_id": self.__vehicle_id,
            "available_in_h": self.__available_in_h,
            "deliveries": [
                {
                    "travel_time_in_h": i.get("travel_time_in_h"),
                    "delivery_info": [
                        {
                            "order_code": j.get("order_code"),
                            "pkg_id": j.get("pkg_id"),
                            "pkg_weight_in_kg": j.get("pkg_weight_in_kg"),
                            "distance_in_km": j.get("distance_in_km"),
                        }
                        for j in i.get("delivery_info")
                    ],
                }
                for i in self.__deliveries
            ],
        }

    def get_delivery_code(self):
        return self.__delivery_code

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_available_in_h(self):
        return float(self.__available_in_h)

    def get_deliveries(self):
        return self.__deliveries
