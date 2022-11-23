import abc

from some_projects.project_testing_library import Validator


class Car(abc.ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.raise_if_len_is_less_than(value, 4, f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.raise_if_num_is_not_in_range(
            value,
            self.minimum_speed_limit,
            self.maximum_speed_limit,
            f"Invalid speed limit! Must be between {self.minimum_speed_limit} and {self.maximum_speed_limit}!")
        self.__speed_limit = value

    @property
    @abc.abstractmethod
    def minimum_speed_limit(self):
        pass

    @property
    @abc.abstractmethod
    def maximum_speed_limit(self):
        pass
