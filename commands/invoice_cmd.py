from commands.command_line import expect_input, mid_sep, separator
from services.orders_requests import query_order_code


def show_invoice(invoice):
    print("\n" + "#" * 20 + "\n")
    print(f"Delivery cost: {invoice.get_delivery_cost()}")
    print(f"Discount: -{invoice.get_discount()}")
    print(f"Total cost: {invoice.get_total_cost()}")
    print("\n" + "#" * 20 + "\n")
    expect_input()


def create_invoice():
    order_code = input("Order code: ")
    order = query_order_code(order_code)
    delivery_info = order.get_delivery_info()
    invoice = []
    for delivery in delivery_info:
        delivery_distance = delivery.get_distance_in_km()
        min_offer_distance = delivery.get_offer().get_min_distance_in_km()
        max_offer_distance = delivery.get_offer().get_max_distance_in_km()

        package_weight = delivery.get_package().get_pkg_weight_in_kg()
        min_offer_weight = delivery.get_offer().get_min_weight_in_kg()
        max_offer_weight = delivery.get_offer().get_max_weight_in_kg()

        discount_percentage = 0
        if min_offer_distance <= delivery_distance <= max_offer_distance:
            if min_offer_weight <= package_weight <= max_offer_weight:
                discount_percentage = delivery.get_offer().get_discount() / 100

        base_delivery_cost = delivery.get_package().get_base_delivery_cost()

        delivery_cost = (
            base_delivery_cost
            + (package_weight * 10)
            + (delivery_distance * 5)
        )

        discount = delivery_cost * discount_percentage
        total_cost = delivery_cost - discount
        invoice.append(
            {
                "delivery_cost": delivery_cost,
                "discount": discount,
                "total_cost": total_cost,
            }
        )
    separator()
    total_order_cost = 0
    for i, val in enumerate(invoice):
        print(f"Delivery cost: {val.get('delivery_cost')}$")
        print(f"Discount: {val.get('discount')}$")
        print(f"Total cost: {val.get('total_cost')}$")
        if i < len(invoice) - 1:
            print("-" * 20)
        total_order_cost += val.get("total_cost")
    print("-" * 20)
    print(f"Total order cost: {total_order_cost}$")
    separator()
    expect_input()
