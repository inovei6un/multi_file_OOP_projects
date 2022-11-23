from some_projects.project_testing_library import Car
from some_projects.project_testing_library import Validator


class Driver:           # stores the info of each driver
    def __init__(self, name: str):
        self.name = name
        self.car = Car
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_len_is_less_than(value.strip(), 1, f"Name should contain at least one character!")
        self.__name = value

    def change_car(self, car: Car):
        car.is_taken = True
        if self.car is None:
            self.car = car
            return f"Driver {self.name} chose the car {car.model}"

        self.car.is_taken = False
        old_model = self.car.model
        self.car = car
        return f"Driver {self.name} changed his car from {old_model} to {car.model}"
