from project_menu.food_orders_app import FoodOrdersApp
from project_menu.meals.starter import Starter
from project_menu.meals.dessert import Dessert
from project_menu.meals.main_dish import MainDish

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))


food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
print(food_orders_app.clients_list)

print(food_orders_app.cancel_order('0899999999'))
food1 = {"Hummus and Avocado Sandwich": 61,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}

print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food1))
print(food_orders_app.finish_order('0899999999'))