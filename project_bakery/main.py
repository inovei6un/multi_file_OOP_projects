from project_bakery.bakery import Bakery

bakery = Bakery('Huevo Bakery')

print(bakery.add_table('OutsideTable', 55, 15))
print(bakery.add_table('OutsideTable', 56, 10))
print(bakery.reserve_table(10))
print(bakery.reserve_table(5))
