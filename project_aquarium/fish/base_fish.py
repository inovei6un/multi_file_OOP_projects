import abc

from some_projects.project_testing_library import Validator


class BaseFish(abc.ABC):
    EAT_INCREASE = 5

    @abc.abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(value, f"Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.raise_if_empty_string(value, f"Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_value_is_0_or_less(value, f"Price cannot be equal to or below zero.")
        self.__price = value

    def eat(self):
        self.size += self.EAT_INCREASE

# TODO maybe i'll have to change the abstract method here
