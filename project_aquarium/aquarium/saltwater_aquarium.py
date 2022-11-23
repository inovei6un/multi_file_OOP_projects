from some_projects.project_testing_library import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 25)

    @property
    def fish_type(self):
        return 'SaltwaterFish'