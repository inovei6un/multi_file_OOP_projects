from some_projects.project_testing_library import MuscleCar
from some_projects.project_testing_library import SportsCar


class CarFactory:
    car_types = {'SportsCar': SportsCar, 'MuscleCar': MuscleCar}

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.car_types:
            raise ValueError('Invalid car type.')
        return self.car_types[car_type](model, speed_limit)

