from classes.inventory import Inventory
from classes.products import Product


if __name__ == "__main__":

    shop = Inventory()
    shop.add(Product("Pen", 5, 10))
    shop.add(Product("Bag", 60, 2))
    shop.add(Product("Notebook", 12, 5))
    shop.find("Pen").sell(4)
    shop.find("Bag").add_stock(1)

    print(shop.by_value())

    # try:
    #     shop.find("Notebook").sell(50)
    # except ValueError as error:
    #     print("error:", error)
    # try:
    #     shop.add(Product("Pen", 7))
    # except ValueError as error:
    #     print("error:", error)
    # try:
    #     shop.find("Bag").price = -3
    # except ValueError as error:
    #     print("error:", error)
    # for product in shop.by_value():
    #     print(product)
    # print("Total:", shop.total_value)