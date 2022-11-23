from some_projects.project_testing_library import Astronaut


class Meteorologist(Astronaut):
    BREATHING_AIR = 15

    def __init__(self, name):
        super().__init__(name, 90)
