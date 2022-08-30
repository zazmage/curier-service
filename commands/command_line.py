def guarantee_int(message):
    integer_input = input(message)
    while not integer_input.isdigit():
        integer_input = input("Please insert a positive integer number: ")
    return int(integer_input)


def guarantee_float(message):
    float_input = input(message)
    while not float_input.isfloat() and float(float_input) > 0:
        float_input = input("Please insert a positive number: ")
    return int(float_input)


def welcome_menu():
    print("###################")
    print("# Courier Service #")
    print("###################\n")
    print("1) Show orders")
    print("2) Show packages")
    print("3) Show offers")
    print("4) Show invoices")
    print("5) Show vehicles")
    print("6) Show deliveries")
    print("7) Create order")
    print("8) Create invoice")
    print("9) Assign deliveries")
    print("0) Exit")


def exit_application():
    print("\nExiting the application...\n")
    return False


def input_selection():
    return guarantee_int("\nType the number of the selected option: ")


def expect_input():
    input("Press enter to continue...")
    print()


def valid_option():
    print("\nPlease select a valid option...\n")
    expect_input()


def separator():
    print("\n" + "#" * 20 + "\n")


def mid_sep():
    print("-" * 20 + "\n" + "-" * 20)


def no_results():
    print("No results...")
