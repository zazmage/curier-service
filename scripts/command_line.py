# Application messages


def welcome_menu():
    print("Courier Service")
    print("1) Show orders")
    print("2) Show packages")
    print("3) Show offers")
    print("4) Create order")
    print("0) Exit")


def exit_application():
    print("Exiting the application...")
    return False


def input_selection():
    return int(input("Type the number of the selected option: "))


def valid_option():
    print("Please select a valid option...")


# Show messages


def show_packages(packages):
    for i in packages.get_packages():
        print(i)


def show_orders(orders):
    for i in orders.get_orders():
        print(i)


def show_offers(offers):
    for i in offers.get_offers():
        print(i)


def show_invoice(invoice):
    print(f"Delivery cost: {invoice.get_delivery_cost()}")
    print(f"Discount: -{invoice.get_discount()}")
    print(f"Total cost: {invoice.get_total_cost()}")
