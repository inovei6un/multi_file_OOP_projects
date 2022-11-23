from project_bakery.drink.tea import Tea
from project_bakery.drink.water import Water


class DrinkFactory:
    @staticmethod
    def create_drink(drink_type: str, name: str, portion: int, brand: str):
        if drink_type == 'Tea':
            return Tea(name, portion, brand)
        if drink_type == "Water":
            return Water(name, portion, brand)
