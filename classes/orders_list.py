from classes.invoice import Invoice
from classes.offer import Offer
from classes.order import Order
from scripts.command_line import show_invoice
from services.orders_requests import load_orders, save_order


class Orders_list:
    def __init__(self) -> None:
        orders = load_orders()
        self.__orders = []
        for i in orders:
            self.__orders.append(
                Order(
                    i.get("pkg_id"),
                    i.get("no_of_packges"),
                    i.get("distance_in_km"),
                    i.get("offer_code"),
                )
            )

    def get_orders(self):
        return self.__orders

    def create_order(self):
        package = input("Package ID: ")
        no_of_packges = input("Number of packages: ")
        distance_in_km = input("Distance in kilometers: ")
        offer = input("Offer ID: ")
        order = Order(package, no_of_packges, distance_in_km, offer)
        self.__orders.append(order.get_order_dict())
        save_order(order.get_order_dict())
        invoice = Invoice(order)
        show_invoice(invoice)
