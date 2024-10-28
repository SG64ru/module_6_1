"""Создаем базовый класс"""

class Animal:
    alive = True    # (живой)
    fed = False     # (накормленный)
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False  # (съедобно)
    def __init__(self, name):
        self.name = name

"""Создаем класс-наследник"""

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True



a1 = Predator('Волк с Уолл-Стрит')
animal2 = Mammal('Хактико')
p1 = Plant('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive, f'- {a1.name} живой')
print(a2.fed, f'- {a2.name} голоден')

animal1.eat(p1)
animal2.eat(p2)
print(a1.alive, f'- {a1.name} помер')
print(a2.fed, f'- {a2.name} сыт')
