class Product:
    def __init__(self, name, price, quantity=0):
        self._name = name
        self._quantity = quantity
        self.__price = self.price = price

    
    @property
    def price(self):
        return self.__price

    
    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("price must be positive")
        self.__price = price


    @property
    def name(self):
        return self._name


    @property
    def quantity(self):
        return self._quantity


    def add_stock(self, stock):
        if stock < 0:
            raise ValueError("Amount nust be positive")
        self._quantity += stock


    def sell(self, amount):
        if amount > self.quantity:
            raise ValueError(f"not enough {self.name}")


    @property
    def total_value(self):
        return self.price * self.quantity


    def __str__(self):
        return f"{self.name}: {self.quantity} X {self.price} = {self.total_value}"

