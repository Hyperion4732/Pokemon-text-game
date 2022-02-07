import random
import copy
from Pclasses import FirePokemon
from Pclasses import WaterPokemon
from Pclasses import EarthPokemon
from Pclasses import FALTPokemon


class EmberSpirit(FirePokemon):
    def Personal_Ability(self, pokemons):
        pokemons[0].health -= 17
        pokemons[1].health -= 17
        pokemons[2].health -= 17
        print('Ember Spirit плюётся огнём во все стороны')


class Ragnaros(FirePokemon):
    def Personal_Ability(self, pokemon):
        pokemon.health -= 30
        print('Ragnaros делает НННЫЫЫЫЫЫЫАААААА(кидает пиробласт)')


class Deathwing(FirePokemon):
    def Personal_Ability(self, pokemons):
        i = random.randrange(0, 2, 1)
        pokemons[i].health -= self.damage
        i = random.randrange(0, 2, 1)
        pokemons[i].health -= self.damage
        print('Deathwing кидает два фаербола')


class Morphling(WaterPokemon):
    def Personal_Ability(self, pokemons):
        Enemy_copy = copy.copy(pokemons[0])
        if (Enemy_copy.numoftargets == 1):
            Enemy_copy.Personal_Ability(pokemons[0])
        elif (Enemy_copy.numoftargets > 1):
            pokemonsred = []
            pokemonsred.append(pokemons[1])
            pokemonsred.append(pokemons[2])
            pokemonsred.append(pokemons[3])
            Enemy_copy.Personal_Ability(pokemonsred)
        elif (Enemy_copy.numoftargets == -1):
            self.Evolution()
        elif (Enemy_copy.numoftargets == 0):
            self.health += 30
            self.damage += 10
            self.armor +=5
            print('Скопировав силы Malfurion, Morphling понял силу природы и впитал её мощь(получил плотные бонусы к здоровью, атаке и броне)')
        print('Morphling превратился в копию соперника, от чего последний безусловно в шоке')


class Slardar(WaterPokemon):
    def Personal_Ability(self, pokemon):
        pokemon.armor -= 8
        print('Slardar неистово один за другим наносит удары трезубцем и разрушает броню противника')


class Murchal(WaterPokemon):
    def Personal_Ability(self, pokemon):
        pokemon.health -= 10
        self.damage += 5
        self.health -= 5
        print('Murchal плюётся жижей в противника и на свой клинок')


class EarthSpirit(EarthPokemon):
    def Personal_Ability(self, pokemon):
        pokemon.health -= 15
        self.armor += 3
        print('Earth Spirit яки Оптимус Прайм складывается в бочку и начинает кататься туда-сюда')


class Malfurion(EarthPokemon):
    def Personal_Ability(self, pokemons):
        for i in range(len(pokemons)):
            pokemons[i].damage += 5
            pokemons[i].health += 20
            pokemons[i].armor += 2
        print('Malfurion посыпает своих тиммейтов росточками и они усиляются')


class Tiny(EarthPokemon):
    def Personal_Ability(self):
        self.Evolution()



class StormSpirit(FALTPokemon):
    def Personal_Ability(self, pokemons):
        for i in range(0, 2):
            pokemons[i].health -= int(self.damage * 0.35)
        for i in range(0, 2):
            pokemons[i].health -= int(self.damage * 0.35)
        print('StormSpirit дважды херачит по вражеской команде молниями из рук')


class Grisha(FALTPokemon):
    def Personal_Ability(self, pokemons):
        i = random.randrange(0, 2, 1)
        pokemons[i].health -= 25
        if (i == 2):
            pokemons[0].health -= 10
            pokemons[1].health -= 10
        if (i == 1):
            pokemons[0].health -= 10
            pokemons[2].health -= 10
        if (i == 0):
            pokemons[1].health -= 10
            pokemons[2].health -= 10
        print('Григорий Дмитриевич кидает бiмбу прямо в сердце вражеской команды')


class TovaristchBurmistrov(FALTPokemon):
    def Personal_Ability(self, pokemon):
        pokemon.damage -= 5
        pokemon.health -= 15
        pokemon.armor -= 4
        pokemon.cd1 += 1
        print('Александр Николаевич насылает порчу на студентика и уходит на перекур')
