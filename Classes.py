class Animal():
    def __init__(self, name):
        self.name = name


class Pokemon(Animal):
    def __init__(self, name, damage, health, armor, cd1, cdtek1, cd2, cdtek2, maxhealth, numoftargets):
        super().__init__(name)
        self.damage = damage
        self.health = health
        self.armor = armor
        self.cd1 = cd1
        self.cdtek1 = cdtek1
        self.cd2 = cd2
        self.cdtek2 = cdtek2
        self.maxhealth = maxhealth
        self.numoftargets = numoftargets

    def Evolution(self):
        self.damage = self.damage + 2
        self.health = self.health + 6
        self.armor = self.armor + 1
        print('О боже, камень эволюционирует!!!!Я в шоке...')

    def INFO(self):
        print(f'Имя:{self.name}')
        print(f'Урон:{self.damage}')
        print(f'Здоровье:{self.health}')
        print(f'Броня:{self.armor}')
        print(f'Ходов до восстановления 1ой способности {self.cdtek1}')
        print(f'Ходов до восстановления 2ой способности {self.cdtek2}')


class Human(Animal):
    pass
