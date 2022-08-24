from classes.offers_list import Offers_list
from classes.orders_list import Orders_list
from classes.packages_list import Packages_list
from commands.command_line import *

if __name__ == "__main__":
    app_running = True
    orders = Orders_list()
    packages = Packages_list()
    offers = Offers_list()
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
            orders.create_order()
        elif selection == 0:
            app_running = exit_application()
        else:
            valid_option()
