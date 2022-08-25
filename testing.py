orders = [
    {"order_code": "ORD001"},
    {"order_code": "ORD002"},
    {"order_code": "ORD003"},
]
orders = [i.get("order_code") for i in orders]
max_number = 0
for i in orders:
    order_code_number = int("".join([j for j in [*i] if j.isnumeric()]))
    if max_number < order_code_number:
        max_number = order_code_number

print(f"ORD{max_number + 1}")
