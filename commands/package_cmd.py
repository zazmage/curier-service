from commands.command_line import expect_input, mid_sep, separator


def show_packages(packages):
    separator()
    for i in packages:
        print("Package ID: ", i.get_pkg_id())
        print("Base delivery cost: ", i.get_base_delivery_cost())
        print("Package weight in kg: ", i.get_pkg_weight_in_kg())
        mid_sep()
    separator()
    expect_input()
