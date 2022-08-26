from commands.command_line import expect_input


def show_offers(offers):
    print("\n" + "#" * 20 + "\n")
    for i in offers:
        print("Offer code: ", i.get_offer_code())
        print("Discount: ", i.get_discount())
        print("Min distance in km: ", i.get_min_distance_in_km())
        print("Max distance in km: ", i.get_max_distance_in_km())
        print("Min weight in kg: ", i.get_min_weight_in_kg())
        print("Min weight in kg: ", i.get_max_weight_in_kg())
        print("\n" + "-" * 20 + "\n" + "-" * 20 + "\n")
    print("#" * 20 + "\n")
    expect_input()
