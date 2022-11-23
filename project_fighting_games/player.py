from unit_testing.library_unittest import Validator


class Player:  # some kind of repository
    used_names = set()
    MIN_STAMINA_VALUE = 0
    MAX_STAMINA_VALUE = 100

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(value, f"Name not valid!")

        if value in self.used_names:
            raise Exception(f"Name {value} is already used!")
        self.used_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError(f"The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.MIN_STAMINA_VALUE or value > self.MAX_STAMINA_VALUE:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
