from unit_testing.library_unittest import Supply


class Food(Supply):

    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    def details(self):
        return f'{Food.__name__}: {self.name}, {self.energy}'
