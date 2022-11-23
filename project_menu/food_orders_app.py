from project_menu.client import Client
from project_menu.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        client = Client(client_phone_number)
        if client.phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception(f"The client has already been registered!")

        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ != 'Starter' and meal.__class__.__name__ != 'MainDish' and meal.__class__.__name__ != 'Dessert':
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")

        result = '\n'.join(m.details() for m in self.menu).strip()

        return result

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.register_client(client_phone_number)

        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")

        client = self.__find_client_by_phone_number(client_phone_number)

        for meal in meal_names_and_quantities:
            current_meal = meal
            current_quantity = meal_names_and_quantities[meal]

            if current_meal not in [m.name for m in self.menu]:
                client.shopping_cart = []
                client.bill = 0.0
                raise Exception(f"{meal} is not on the menu!")

            for m in self.menu:
                if current_meal == m.name:
                    if current_quantity > m.quantity:
                        client.shopping_cart = []
                        client.bill = 0.0
                        raise Exception(f"Not enough quantity of {m.__class__.__name__}: {m.name}!")
                    m.quantity -= current_quantity
                    client.shopping_cart.append(m)
                    client.bill += current_quantity * m.price

        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."

            # TODO May add meal types that are not Starter and etc.

    def cancel_order(self, client_phone_number):
        client = self.__find_client_by_phone_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception(f"There are no ordered meals!")

        for meal in client.shopping_cart:
            for m in self.menu:
                if meal.name == m.name:
                    m.quantity += meal.quantity

        client.shopping_cart = []
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.__find_client_by_phone_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception(f"There are no ordered meals!")

        receipt = 0
        total_paid_money = client.bill

        client.shopping_cart = []
        client.bill = 0.0

        return f"Receipt #{receipt + 1} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __find_client_by_phone_number(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client
