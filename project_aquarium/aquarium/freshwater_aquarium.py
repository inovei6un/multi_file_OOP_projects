from some_projects.project_testing_library import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 50)

    @property
    def fish_type(self):
        return 'FreshwaterFish'
