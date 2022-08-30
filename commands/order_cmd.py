from commands.command_line import (
    expect_input,
    guarantee_float,
    guarantee_int,
    mid_sep,
    no_results,
    separator,
)
from services.order_requests import save_order


def show_orders(orders):
    separator()
    if orders:
        for i in orders:
            print("Order code: ", i.get_order_code())
            print("Number of packages: ", i.get_no_of_packges())
            print("Delivery info: ")
            for j in i.get_delivery_info():
                print(
                    "---> Package ID: ",
                    j.get("package").get_pkg_id(),
                )
                print(
                    "---> Distance in km: ",
                    j.get("distance_in_km"),
                )
                print("---> Offer code: ", j.get("offer").get_offer_code())
                print("-")
            mid_sep()
        separator()
    else:
        no_results()
    expect_input()


def create_order(packages, offers):
    pkg_id_list = [i.get_pkg_id() for i in packages]
    offer_code_list = [i.get_offer_code() for i in offers]
    no_of_packges = guarantee_int("Number of packages: ")
    delivery_info = []
    for i in range(1, no_of_packges + 1):
        pkg_id = input(f"Package {i} ID: ")
        while pkg_id not in pkg_id_list:
            pkg_id = input(
                "The package was not found, please enter a valid ID: "
            )
        distance_in_km = guarantee_float(
            f"Package {i} distance in kilometers: "
        )
        offer_code = input(f"Package {i} Offer ID: ")
        while offer_code not in offer_code_list:
            offer_code = input(
                "The offer was not found, please enter a valid code: "
            )
        delivery_info.append(
            {
                "pkg_id": pkg_id,
                "distance_in_km": distance_in_km,
                "offer_code": offer_code,
            }
        )
    save_order(no_of_packges, delivery_info)
