from Classes import Pokemon


class WaterPokemon(Pokemon):
    def Special_fight(self, pokemon):
        self.health += 10
        pokemon.health -= 10
        print(f'{self.name} отсасывает жизни у {pokemon.name}')


class FirePokemon(Pokemon):
    def Special_fight(self, pokemon):
        pokemon.health -= 20
        print(f'{self.name} кидает фаербол {pokemon.name} прямо в лицо')


class EarthPokemon(Pokemon):
    def Special_fight(self, pokemon):
        self.health += 5
        self.armor += 3
        pokemon.health -= 5
        print(f'{self.name} плюётся грязью в {pokemon.name}')

class FALTPokemon(Pokemon):
    def Special_fight(self, pokemon):
        pokemon.health -= self.damage - pokemon.armor
        pokemon.health -= self.damage - pokemon.armor
        print(f'{self.name} пикирует в {pokemon.name}')
