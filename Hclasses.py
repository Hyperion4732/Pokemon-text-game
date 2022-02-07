from Classes import Human


class Master(Human):
    def __init__(self, name, intelligence, stamina):
        super().__init__(name)
        self.intelligence = intelligence
        self.stamina = stamina


class Doctor(Human):
    def __init__(self, name, healstrength, usages):
        super().__init__(name)
        self.healstrength = healstrength
        self.usages = usages

    def HealPokemon(self, pokemon):
        if (pokemon.health + self.healstrength > pokemon.maxhealth):
            pokemon.health = pokemon.maxhealth
        else:
            pokemon.health += self.healstrength


class Spectator(Human):
    def __init__(self, name, support, usages):
        super().__init__(name)
        self.support = support
        self.usages = usages

    def Сheerup(self, pokemon):
        pokemon.damage += self.support

    def Boo(self, pokemon):
        pokemon.damage -= self.support
