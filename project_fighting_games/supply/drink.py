from unit_testing.library_unittest import Supply


class Drink(Supply):

    def __init__(self, name):
        super().__init__(name, 15)

    def details(self):
        return f'{Drink.__name__}: {self.name}, {self.energy}'
