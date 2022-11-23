import abc

from some_projects.project_testing_library import Validator


class Astronaut(abc.ABC):
    BREATHING_AIR = 10

    @abc.abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_whites_space(value, f"Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.BREATHING_AIR

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        result = f"Name: {self.name}" + '\n'
        result += f"Oxygen: {self.oxygen}" + '\n'
        result += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}" + '\n'

        return result
