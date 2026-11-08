from .products import Product


class Inventory:
    def  __init__(self):
        self._products = []


    def add(self, product):
        if product in self._products:
            raise ValueError(f"{product.name} alreaedy exists")
        self._products.append(product)


    def find(self, name):
        for p in self._products:
            if p.name == name:
                return p
        return None


    def by_value(self):
        return sorted(self._products, key= lambda p: p.total_value, reverse=True)

    
    @property
    def total_value(self):
        return sum([p.total_value for p in self._products])


    def low_stock(self, limit):
        return filter(lambda p: p.quantity < limit, self._products)
    