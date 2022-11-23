from some_projects.project_testing_library import Controller

controller = Controller()
print(controller.add_decoration('Plant'))

print(controller.add_aquarium('FreshwaterAquarium', 'Aquarium'))
print(controller.add_fish('Aquarium', 'FreshwaterFish', 'Nemo', 'Goldfish', 2.50))
