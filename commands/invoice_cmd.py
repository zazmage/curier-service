from commands.command_line import expect_input, mid_sep, separator
from services.invoice_requests import save_invoice
from services.order_requests import query_order


def show_invoice(invoice_info, total_order_cost):
    separator()
    for i in invoice_info:
        print(f"Delivery cost: {i.get('delivery_cost')}$")
        print(f"Discount: {i.get('discount')}$")
        print(f"Total cost: {i.get('total_cost')}$")
        print("-" * 20)
    print(f"Total order cost: {total_order_cost}$")
    separator()
    expect_input()


def show_invoices(invoices):
    separator()
    for i in invoices:
        print(f"Invoice code: {i.get_invoice_code()}")
        print(f"Order code: {i.get_order_code()}")
        print("Invoice info: ")
        for j in i.get_invoice_info():
            print(
                "---> Delivery cost: ",
                j.get("delivery_cost"),
            )
            print(
                "---> Discount: ",
                j.get("discount"),
            )
            print(f"---> Total cost: {j.get('total_cost')}$")
            print("-" * 20)
        print(f"Total order cost: {i.get_total_order_cost()}$")
        mid_sep()

    separator()
    expect_input()


def create_invoice():
    order_code = input("Order code: ")
    order = query_order(order_code)
    delivery_info = order.get_delivery_info()
    invoice_info = []
    total_order_cost = 0
    for i in delivery_info:
        delivery_distance = i.get("distance_in_km")
        min_offer_distance = i.get("offer").get_min_distance_in_km()
        max_offer_distance = i.get("offer").get_max_distance_in_km()

        package_weight = i.get("package").get_pkg_weight_in_kg()
        min_offer_weight = i.get("offer").get_min_weight_in_kg()
        max_offer_weight = i.get("offer").get_max_weight_in_kg()

        discount_percentage = 0
        if min_offer_distance <= delivery_distance <= max_offer_distance:
            if min_offer_weight <= package_weight <= max_offer_weight:
                discount_percentage = i.get("offer").get_discount() / 100

        base_delivery_cost = i.get("package").get_base_delivery_cost()

        delivery_cost = (
            base_delivery_cost
            + (package_weight * 10)
            + (delivery_distance * 5)
        )

        discount = delivery_cost * discount_percentage
        total_cost = delivery_cost - discount
        total_order_cost += total_cost
        invoice_info.append(
            {
                "delivery_cost": delivery_cost,
                "discount": discount,
                "total_cost": total_cost,
            }
        )

    save_invoice(order_code, invoice_info, total_order_cost)
    show_invoice(invoice_info, total_order_cost)
