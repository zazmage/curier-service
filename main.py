from commands.command_line import (
    exit_application,
    input_selection,
    valid_option,
    welcome_menu,
)
from commands.invoice_cmd import create_invoice, show_invoices
from commands.offer_cmd import show_offers
from commands.order_cmd import create_order, show_orders
from commands.package_cmd import show_packages
from services.invoice_requests import load_invoices
from services.offer_requests import load_offers
from services.order_requests import load_orders
from services.package_requests import load_packages

if __name__ == "__main__":
    app_running = True
    orders = load_orders()
    packages = load_packages()
    offers = load_offers()
    invoices = load_invoices()

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
            create_order()
            orders = load_orders()
        elif selection == 6:
            create_invoice()
            invoices = load_invoices()
        elif selection == 0:
            app_running = exit_application()
        else:
            valid_option()
