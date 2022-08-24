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


def expect_input():
    input("Press enter to continue...")
    print()


def valid_option():
    print("Please select a valid option...")


# Show messages


def show_packages(packages):
    print("\n" + "#" * 20 + "\n")
    for i in packages.get_packages():
        print("Package ID: ", i.get_pkg_id())
        print("Base delivery cost: ", i.get_base_delivery_cost())
        print("Package weight in kg: ", i.get_pkg_weight_in_kg())
        print("\n" + "-" * 20 + "\n" + "-" * 20 + "\n")
    print("#" * 20 + "\n")
    expect_input()


def show_orders(orders):
    print("\n" + "#" * 20 + "\n")
    for i in orders.get_orders():
        print("Package ID: ", i.get_pkg_id())
        print("Number of packages: ", i.get_no_of_packges())
        print("Distance in km: ", i.get_distance_in_km())
        print("Offer code: ", i.get_offer_code())
        print("\n" + "-" * 20 + "\n" + "-" * 20 + "\n")
    print("#" * 20 + "\n")
    expect_input()


def show_offers(offers):
    print("\n" + "#" * 20 + "\n")
    for i in offers.get_offers():
        print("Offer code: ", i.get_offer_code())
        print("Discount: ", i.get_discount())
        print("Min distance in km: ", i.get_min_distance_in_km())
        print("Max distance in km: ", i.get_max_distance_in_km())
        print("Min weight in kg: ", i.get_min_weight_in_kg())
        print("Min weight in kg: ", i.get_max_weight_in_kg())
        print("\n" + "-" * 20 + "\n" + "-" * 20 + "\n")
    print("#" * 20 + "\n")
    expect_input()


def show_invoice(invoice):
    print("\n" + "#" * 20 + "\n")
    print(f"Delivery cost: {invoice.get_delivery_cost()}")
    print(f"Discount: -{invoice.get_discount()}")
    print(f"Total cost: {invoice.get_total_cost()}")
    print("\n" + "#" * 20 + "\n")
    expect_input()
