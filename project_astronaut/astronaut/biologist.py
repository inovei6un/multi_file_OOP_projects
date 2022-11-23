from some_projects.project_testing_library import Astronaut


class Biologist(Astronaut):
    BREATHING_AIR = 5

    def __init__(self, name):
        super().__init__(name, 70)
