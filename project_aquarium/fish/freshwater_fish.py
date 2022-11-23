from some_projects.project_testing_library import BaseFish


class FreshwaterFish(BaseFish):
    EAT_INCREASE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += self.EAT_INCREASE
        return self.size

# can only live in freshwater aquarium
