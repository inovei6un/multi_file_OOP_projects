from some_projects.project_testing_library import Ornament
from some_projects.project_testing_library import Plant


class DecorationFactory:
    decoration_types = {"Ornament": Ornament, 'Plant': Plant}

    def create_decoration(self, decoration_type: str):
        if decoration_type not in self.decoration_types:
            raise ValueError(f"Invalid decoration type.")
        return self.decoration_types[decoration_type]()
