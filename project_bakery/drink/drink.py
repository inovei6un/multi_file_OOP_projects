import abc

from project_bakery.validator.validator import Validator


class Drink(abc.ABC):
    @abc.abstractmethod
    def __init__(self, name: str, portion: int, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_whitespace(value, f'Name cannot be empty string or white space!')
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        Validator.raise_if_value_is_0_or_less(value, f"Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.raise_if_empty_string_or_whitespace(value, f"Brand cannot be empty string or white space!")
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
