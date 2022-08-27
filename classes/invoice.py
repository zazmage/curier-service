class Invoice:
    def __init__(
        self, invoice_code, order_code, invoice_info, total_order_cost
    ):
        self.__invoice_code = invoice_code
        self.__order_code = order_code
        self.__invoice_info = invoice_info
        self.__total_order_cost = total_order_cost

    def get_invoice_dict(self):
        return {
            "invoice_code": self.__invoice_code,
            "order_code": self.__order_code,
            "invoice_info": [
                {
                    "delivery_cost": i.get("delivery_cost"),
                    "discount": i.get("discount"),
                    "total_cost": i.get("total_cost"),
                }
                for i in self.__invoice_info
            ],
            "total_order_cost": self.__total_order_cost,
        }

    def get_invoice_code(self):
        return self.__invoice_code

    def get_order_code(self):
        return self.__order_code

    def get_invoice_info(self):
        return self.__invoice_info

    def get_total_order_cost(self):
        return self.__total_order_cost
