from some_projects.project_testing_library import Car


class MuscleCar(Car):
    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def minimum_speed_limit(self):
        return 250

    @property
    def maximum_speed_limit(self):
        return 450
