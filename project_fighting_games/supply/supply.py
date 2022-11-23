import abc

from unit_testing.library_unittest import Validator


class Supply(abc.ABC):

    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(value, f"Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validator.raise_if_value_is_negative(value, f"Energy cannot be less than zero.")
        self.__energy = value

    @abc.abstractmethod
    def details(self):
        pass
