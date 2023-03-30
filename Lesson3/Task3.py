products = []


def show_task():
    print(
        'Enter the name of the product, price, quantity and unit of measure '
        'in one line')
    print('Use a comma as a position separator')
    print('Price and quantity values must be integer')
    print('Enter key enter to exit cycle')


def show_all_products(products_arg):
    number = 0
    while True:
        number += 1
        product_list = input(f'{number} product: ').split(',')
        if product_list == ['']:
            break

        products_arg.append((number, {'Name': product_list[0],
                                      'Price': int(product_list[1]),
                                      'Count': int(product_list[2]),
                                      'Unit of measure': product_list[3]}))

    print(f"Original list of products: \n{products_arg}")


def show_product_report(products_arg):
    products_dict = {}
    for i, el in enumerate(list(products_arg[0][1].keys())):
        products_dict[el] = []

    for i, el in enumerate(products_dict):
        dict_list = []

        for j, el_goods in enumerate(products_arg):
            key_val = el_goods[1].get(el)
            if key_val not in dict_list:
                dict_list.append(key_val)

        products_dict[el] = dict_list

    print("Product list report: ")
    for k, v in products_dict.items():
        print(k, v)


show_task()
show_all_products(products)
show_product_report(products)
