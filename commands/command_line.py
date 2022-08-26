def guarantee_int(message):
    integer_input = input(message)
    while not integer_input.isdigit():
        integer_input = input("Please insert a positive integer number: ")
    return int(integer_input)


def welcome_menu():
    print("Courier Service")
    print("1) Show orders")
    print("2) Show packages")
    print("3) Show offers")
    print("4) Create order")
    print("5) Create invoice")
    print("0) Exit")


def exit_application():
    print("Exiting the application...")
    return False


def input_selection():
    return guarantee_int("Type the number of the selected option: ")


def expect_input():
    input("Press enter to continue...")
    print()


def valid_option():
    print("Please select a valid option...")


def separator():
    print("\n" + "#" * 20 + "\n")


def mid_sep():
    print("-" * 20 + "\n" + "-" * 20)
