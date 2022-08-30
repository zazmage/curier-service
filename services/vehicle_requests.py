import json
from classes.vehicle import Vehicle


def load_vehicles():
    try:
        with open("./databases/vehicles.json", "r") as file:
            vehicles = json.loads(file.read())

            vehicles_list = [
                Vehicle(
                    i.get("vehicle_id"),
                    float(i.get("max_speed_in_kmh")),
                    float(i.get("max_load_in_kg")),
                    float(i.get("actual_load_in_kg")),
                    float(i.get("available_in_h")),
                    i.get("deliveries"),
                )
                for i in vehicles
            ]
            return vehicles_list
    except:
        return []


def query_veicles_list(vehicle_id_list):
    try:
        with open("./databases/vehicles.json", "r") as file:
            vehicles = json.loads(file.read())

            vehicles_list = [
                Vehicle(
                    i.get("vehicle_id"),
                    float(i.get("max_speed_in_kmh")),
                    float(i.get("max_load_in_kg")),
                    float(i.get("actual_load_in_kg")),
                    float(i.get("available_in_h")),
                    i.get("deliveries"),
                )
                for i in vehicles
            ]
            vehicles_list = [
                i
                for i in vehicles_list
                if i.get_vehicle_id() in vehicle_id_list
            ]
            return vehicles_list
    except:
        return []


def query_vehicle(vehicle_id):
    try:
        with open("./databases/vehicles.json", "r") as file:
            vehicles = json.loads(file.read())

            vehicles_list = [
                Vehicle(
                    i.get("vehicle_id"),
                    float(i.get("max_speed_in_kmh")),
                    float(i.get("max_load_in_kg")),
                    float(i.get("actual_load_in_kg")),
                    float(i.get("available_in_h")),
                    i.get("deliveries"),
                )
                for i in vehicles
            ]
            vehicle = next(
                (i for i in vehicles_list if i.get_vehicle_id() == vehicle_id),
                None,
            )
            return vehicle
    except:
        return None


def update_vehicle_status(
    vehicle_id, actual_load_in_kg, available_in_h, deliveries
):
    try:
        with open("./databases/vehicles.json", "r+") as file:
            vehicles = load_vehicles()
            vehicles = [i.get_vehicle_dict() for i in vehicles]
            vehicle = next(
                (i for i in vehicles if i.get("vehicle_id") == vehicle_id),
                None,
            )
            vehicle_index = vehicles.index(vehicle)
            vehicles[vehicle_index] = {
                "vehicle_id": vehicle.get("vehicle_id"),
                "max_speed_in_kmh": vehicle.get("vehicle_id"),
                "max_load_in_kg": vehicle.get("vehicle_id"),
                "actual_load_in_kg": actual_load_in_kg,
                "available_in_h": available_in_h,
                "deliveries": deliveries,
            }
            file.seek(0)
            json.dump(vehicles, file, indent=2)
            print("\nSuccessfully updated vehicle...")
    except:
        print("Something went wrong...")
