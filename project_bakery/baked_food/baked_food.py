import abc
from project_bakery.validator.validator import Validator


class BakedFood(abc.ABC):
    
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_whitespace(value, f'Name cannot be empty string or white space!')
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_value_is_0_or_less(value, f"Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
