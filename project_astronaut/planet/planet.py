from some_projects.project_testing_library import Validator


class Planet:

    def __init__(self, name: str):
        self.name = name

        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_whites_space(value, f"Planet name cannot be empty string or whitespace!")
        self.__name = value
