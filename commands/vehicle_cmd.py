from commands.command_line import expect_input, mid_sep, separator


def show_vehicles(vehicles):
    separator()
    for i in vehicles:
        print("Vehicle ID: ", i.get_vehicle_id())
        print("Max speed in km/h: ", i.get_max_speed_in_kmh())
        print("Max load in kg: ", i.get_max_load_in_kg())
        print("Actual load in kg: ", i.get_actual_load_in_kg())
        print("Available in h: ", i.get_available_in_h())
        mid_sep()
    separator()
    expect_input()
