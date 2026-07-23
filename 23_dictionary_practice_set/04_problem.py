# Given a dictionary of products and their prices, find the product with the highest price

products = {
    "colgate" :  30,
    "water"   :  20,
    "bag"     :  10
}

highest_price = 0
highest_product = ""

for product,price in products.items():
    if price>highest_price:
        highest_price = price
        highest_product = product


print(f"product with highest price = {highest_product}:{highest_price}")

