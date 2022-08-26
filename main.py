from commands.command_line import (
    exit_application,
    input_selection,
    valid_option,
    welcome_menu,
)
from commands.offer_cmd import show_offers
from commands.order_cmd import create_order, show_orders
from commands.package_cmd import show_packages
from services.offers_requests import load_offers
from services.orders_requests import load_orders
from services.packages_requests import load_packages

if __name__ == "__main__":
    app_running = True
    orders = load_orders()
    packages = load_packages()
    offers = load_offers()
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
            create_order()
            orders = load_orders()
        elif selection == 5:
            create_invoice()
        elif selection == 0:
            app_running = exit_application()
        else:
            valid_option()
