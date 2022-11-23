from some_projects.project_testing_library import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    def find_astronauts_for_mission(self, count, min_oxygen):
        return sorted([a for a in self.astronauts if a.oxygen > min_oxygen],
                      key=lambda x: x.oxygen,
                      reverse=True)[0:count]
