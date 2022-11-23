from some_projects.project_testing_library import FreshwaterFish
from some_projects.project_testing_library import SaltwaterFish


class FishFactory:
    fish_types = {'FreshwaterFish': FreshwaterFish, 'SaltwaterFish': SaltwaterFish}

    def create_fish(self, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.fish_types:
            raise ValueError(f"There isn't a fish of type {fish_type}")

        return self.fish_types[fish_type](fish_name, fish_species, price)
