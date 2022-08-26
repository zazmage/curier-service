from commands.command_line import expect_input, guarantee_int
from services.orders_requests import query_order_code


def show_invoice(invoice):
    print("\n" + "#" * 20 + "\n")
    print(f"Delivery cost: {invoice.get_delivery_cost()}")
    print(f"Discount: -{invoice.get_discount()}")
    print(f"Total cost: {invoice.get_total_cost()}")
    print("\n" + "#" * 20 + "\n")
    expect_input()


def create_invoice():
    order_code = guarantee_int("Order code: ")
    order = query_order_code(order_code)

    discount = 0

    order_distance = order.get_delivery_info().get_distance_in_km()
    min_offer_distance = order.get_offer().get_min_distance_in_km()
    max_offer_distance = order.get_offer().get_max_distance_in_km()

    order_weight = order.get_package().get_pkg_weight_in_kg()
    min_offer_weight = order.get_offer().get_min_weight_in_kg()
    max_offer_weight = order.get_offer().get_max_weight_in_kg()

    discount_percentage = 0
    if min_offer_distance <= order_distance <= max_offer_distance:
        if min_offer_weight <= order_weight <= max_offer_weight:
            discount_percentage = order.get_offer().get_discount() / 100

    base_delivery_cost = order.get_package().get_base_delivery_cost()

    delivery_cost = (
        base_delivery_cost + (order_weight * 10) + (order_distance * 5)
    )

    discount = delivery_cost * discount_percentage

    total_cost = delivery_cost - discount
