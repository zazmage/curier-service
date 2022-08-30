import json

from classes.delivery import Delivery
from services.offer_requests import query_offer
from services.package_requests import query_package
from utils.utils import new_code


def load_delieveries():
    try:
        with open("./databases/deliveries.json", "r") as file:
            deliveries = json.loads(file.read())
            if deliveries:
                deliveries_list = [
                    Delivery(
                        i.get("delivery_code"),
                        i.get("vehicle_id"),
                        i.get("available_in_h"),
                        [
                            {
                                "travel_time_in_h": j.get("travel_time_in_h"),
                                "delivery_info": [
                                    {
                                        "order_code": k.get("order_code"),
                                        "pkg_id": k.get("pkg_id"),
                                        "pkg_weight_in_kg": k.get(
                                            "pkg_weight_in_kg"
                                        ),
                                        "distance_in_km": k.get(
                                            "distance_in_km"
                                        ),
                                    }
                                    for k in j.get("delivery_info")
                                ],
                            }
                            for j in i.get("deliveries")
                        ],
                    )
                    for i in deliveries
                ]
                return deliveries_list
            return []
    except:
        return []


def query_delivery(delivery_code):
    try:
        with open("./databases/deliveries.json", "r") as file:
            deliveries = json.loads(file.read())
            deliveries_list = [
                Delivery(
                    i.get("delivery_code"),
                    i.get("vehicle_id"),
                    i.get("available_in_h"),
                    [
                        {
                            "travel_time_in_h": j.get("travel_time_in_h"),
                            "delivery_info": [
                                {
                                    "order_code": k.get("order_code"),
                                    "pkg_id": k.get("pkg_id"),
                                    "pkg_weight_in_kg": k.get(
                                        "pkg_weight_in_kg"
                                    ),
                                    "distance_in_km": k.get("distance_in_km"),
                                }
                                for k in j.get("delivery_info")
                            ],
                        }
                        for j in i.get("deliveries")
                    ],
                )
                for i in deliveries
            ]
            delivery = next(
                (
                    i
                    for i in deliveries_list
                    if i.get_delivery_code() == delivery_code
                ),
                None,
            )
            return delivery
    except:
        return None


def save_delivery(vehicle_id, available_in_h, deliveries):
    try:
        with open("./databases/deliveries.json", "r+") as file:
            deliveries_list = load_delieveries()
            if deliveries_list:
                delivery = {
                    "delivery_code": new_code(
                        "DLY", [i.get_delivery_code() for i in deliveries_list]
                    ),
                    "vehicle_id": vehicle_id,
                    "available_in_h": available_in_h,
                    "deliveries": deliveries,
                }
                deliveries_list = [
                    i.get_delivery_dict() for i in deliveries_list
                ]
                deliveries_list.append(delivery)
                file.seek(0)
                json.dump(deliveries_list, file, indent=2)
                print("Successfully created delivery...")
            else:
                json.dump(
                    [
                        {
                            "delivery_code": new_code("DLY", []),
                            "vehicle_id": vehicle_id,
                            "available_in_h": available_in_h,
                            "deliveries": deliveries,
                        }
                    ],
                    file,
                    indent=2,
                )
                print("Successfully created delivery...")
    except:
        print("Something went wrong...")
