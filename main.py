from commands.command_line import (
    exit_application,
    input_selection,
    valid_option,
    welcome_menu,
)
from commands.delivery_cmd import assign_deliveries, show_deliveries
from commands.invoice_cmd import create_invoice, show_invoices
from commands.offer_cmd import show_offers
from commands.order_cmd import create_order, show_orders
from commands.package_cmd import show_packages
from commands.vehicle_cmd import show_vehicles
from services.delivery_requests import load_delieveries
from services.invoice_requests import load_invoices
from services.offer_requests import load_offers
from services.order_requests import load_orders
from services.package_requests import load_packages
from services.vehicle_requests import load_vehicles

if __name__ == "__main__":
    app_running = True
    orders = load_orders()
    packages = load_packages()
    offers = load_offers()
    invoices = load_invoices()
    vehicles = load_vehicles()
    deliveries = load_delieveries()

    while app_running:
        welcome_menu()
        selection = input_selection()
        if selection == 1:
            show_orders(orders)
        elif selection == 2:
            show_packages(packages)
        elif selection == 3:
            show_offers(offers)
        elif selection == 4:
            show_invoices(invoices)
        elif selection == 5:
            show_vehicles(vehicles)
        elif selection == 6:
            show_deliveries(deliveries)
        elif selection == 7:
            create_order(packages, offers)
            orders = load_orders()
        elif selection == 8:
            create_invoice(orders)
            invoices = load_invoices()
        elif selection == 9:
            assign_deliveries(orders, vehicles)
        elif selection == 0:
            app_running = exit_application()
        else:
            valid_option()
