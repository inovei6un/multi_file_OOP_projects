from project_bakery.baked_food.bread import Bread
from project_bakery.baked_food.cake import Cake


class FoodFactory:
    @staticmethod
    def create_food(food_type: str, name: str, price: float):
        if food_type == 'Cake':
            return Cake(name, price)
        if food_type == "Bread":
            return Bread(name, price)
