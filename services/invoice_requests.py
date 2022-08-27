import json
from classes.invoice import Invoice
from utils.utils import new_code


def load_invoices():
    try:
        with open("./databases/invoices.json", "r") as file:
            invoices = json.loads(file.read())

            invoices_list = [
                Invoice(
                    i.get("invoice_code"),
                    i.get("order_code"),
                    [
                        {
                            "delivery_cost": j.get("delivery_cost"),
                            "discount": j.get("discount"),
                            "total_cost": j.get("total_cost"),
                        }
                        for j in i.get("invoice_info")
                    ],
                    i.get("total_order_cost"),
                )
                for i in invoices
            ]
            return invoices_list
    except:
        return []


def query_invoices_list(invoice_code_list):
    try:
        with open("./databases/invoices.json", "r") as file:
            invoices = json.loads(file.read())
            invoices_list = [
                Invoice(
                    i.get("invoice_code"),
                    i.get("order_code"),
                    [
                        {
                            "delivery_cost": j.get("delivery_cost"),
                            "discount": j.get("discount"),
                            "total_cost": j.get("total_cost"),
                        }
                        for j in i.get("invoice_info")
                    ],
                    i.get("total_order_cost"),
                )
                for i in invoices
            ]
            invoices_list = [
                i
                for i in invoices_list
                if i.get_invoice_code() in invoice_code_list
            ]
            return invoices_list
    except:
        return []


def query_invoice(invoice_code):
    try:
        with open("./databases/invoices.json", "r") as file:
            invoices = json.loads(file.read())
            invoices_list = [
                Invoice(
                    i.get("invoice_code"),
                    i.get("order_code"),
                    [
                        {
                            "delivery_cost": j.get("delivery_cost"),
                            "discount": j.get("discount"),
                            "total_cost": j.get("total_cost"),
                        }
                        for j in i.get("invoice_info")
                    ],
                    i.get("total_order_cost"),
                )
                for i in invoices
            ]
            invoice = next(
                (
                    i
                    for i in invoices_list
                    if i.get_invoice_code() == invoice_code
                ),
                None,
            )
            return invoice
    except:
        return None


def save_invoice(order_code, invoice_info, total_order_cost):
    try:
        with open("./databases/invoices.json", "r+") as file:
            invoices = load_invoices()
            invoice = {
                "invoice_code": new_code(
                    "INV", [i.get_invoice_code() for i in invoices]
                ),
                "order_code": order_code,
                "invoice_info": [
                    {
                        "delivery_cost": i.get("delivery_cost"),
                        "discount": i.get("discount"),
                        "total_cost": i.get("total_cost"),
                    }
                    for i in invoice_info
                ],
                "total_order_cost": total_order_cost,
            }
            invoices = [i.get_invoice_dict() for i in invoices]
            invoices.append(invoice)
            file.seek(0)
            json.dump(invoices, file, indent=2)
            print("\nSuccessfully created invoice...")
    except:
        print("Something went wrong...")
