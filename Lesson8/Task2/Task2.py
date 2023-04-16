import json


def write_order_to_json(item, quantity, price, buyer, date):

    new_value = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json') as fr_n:
        obj = json.load(fr_n)

    obj["orders"].append(new_value)

    with open('orders.json', 'w', encoding='utf-8') as fw_n:
        json.dump(obj, fw_n, indent=4)


write_order_to_json("scaner", "5", "1000", "Nastya Boyarin", "15.04.2023")
