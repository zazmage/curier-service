from commands.command_line import expect_input


def show_packages(packages):
    print("\n" + "#" * 20 + "\n")
    for i in packages:
        print("Package ID: ", i.get_pkg_id())
        print("Base delivery cost: ", i.get_base_delivery_cost())
        print("Package weight in kg: ", i.get_pkg_weight_in_kg())
        print("\n" + "-" * 20 + "\n" + "-" * 20 + "\n")
    print("#" * 20 + "\n")
    expect_input()
