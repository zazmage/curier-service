from classes.delivery_info import Delivery_info
from classes.invoice import Invoice
from classes.order import Order
from commands.command_line import show_invoice
from services.orders_requests import load_orders, save_order


class Orders_list:
    def __init__(self) -> None:
        self.__orders = load_orders()

    def get_orders(self):
        return self.__orders

    def create_order(self):
        no_of_packges = input("Number of packages: ")
        while no_of_packges.isdigit():
            no_of_packges = input("Please insert a positive integer number: ")
        delivery_info = []
        for i in range(1, no_of_packges + 1):
            pkg_id = input(f"Package {i} ID: ")
            distance_in_km = input("Package {i} distance in kilometers: ")
            offer_code = input("Package {i} Offer ID: ")
            delivery_info.append(
                Delivery_info(pkg_id, distance_in_km, offer_code)
            )
        order = Order(no_of_packges, delivery_info)
        self.__orders.append(order.get_order_dict())
        # save_order(order.get_order_dict())
        invoice = Invoice(order)
        show_invoice(invoice)
