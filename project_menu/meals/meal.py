import abc


class Meal(abc.ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError(f"Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return  self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError(f"Invalid price!")
        self.__price = value

    @abc.abstractmethod
    def details(self):
        pass
