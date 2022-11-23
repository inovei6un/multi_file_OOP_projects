import abc

from project_bakery.baked_food.baked_food import BakedFood
from project_bakery.drink.drink import Drink
from project_bakery.validator.validator import Validator


class Table(abc.ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.raise_if_number_is_not_in_range(value,
                                                  self.min_table_number,
                                                  self.max_table_number,
                                                  self.table_number_error_msg)
        self.__table_number = value

    @property
    @abc.abstractmethod
    def min_table_number(self):
        pass

    @property
    @abc.abstractmethod
    def max_table_number(self):
        pass

    @property
    @abc.abstractmethod
    def table_number_error_msg(self):
        pass

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_value_is_0_or_less(value, f"Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.food_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" + \
                   f"Type: {self.__class__.__name__}\n" + \
                   f"Capacity: {self.capacity}"
