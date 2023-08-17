import os
import product
def get_objects():
    product_list =[]
    with open("inventory_list.txt") as f:
        all_products = f.readlines()
    for product in all_products:
        gender, product_type, brand, size, price, quantity = product.split(',')
        product_list.append(product(gender, product_type, brand, size, float(price), int(quantity)))

    return product_list


print(get_objects())


