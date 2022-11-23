from some_projects.project_testing_library import BaseFish


class SaltwaterFish(BaseFish):
    EAT_INCREASE = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += self.EAT_INCREASE
        return self.size

# can only live in saltwater aquarium
