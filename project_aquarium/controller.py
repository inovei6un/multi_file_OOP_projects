from some_projects.project_testing_library import AquariumFactory
from some_projects.project_testing_library import DecorationFactory
from some_projects.project_testing_library import FishFactory
from some_projects.project_testing_library import DecorationRepository


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

        self.aquarium_factory = AquariumFactory()
        self.decoration_factory = DecorationFactory()
        self.fish_factory = FishFactory()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        try:
            aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        except ValueError as error:
            return str(error)

    def add_decoration(self, decoration_type):
        try:
            decoration = self.decoration_factory.create_decoration(decoration_type)
            self.decorations_repository.add(decoration)
            return F"Successfully added {decoration_type}."
        except ValueError as error:
            return str(error)

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}"

        self.decorations_repository.remove(decoration)
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return  # NOT SURE
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        try:
            fish = self.fish_factory.create_fish(fish_type, fish_name, fish_species, price)
            aquarium = self.__find_aquarium_by_name(aquarium_name)
            return aquarium.add_fish(fish)   # takes from base aquarium

        except ValueError as error:
            return error

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        value = sum(f.price for f in aquarium.fish) + sum(d.price for d in aquarium.decorations)
        return f"The value of Aquarium {aquarium.name} is {value:.2f}"

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'
        return result.strip()

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None
