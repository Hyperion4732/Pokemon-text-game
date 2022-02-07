from Team import *
from Hclasses import *
from Abilities import *
import pygame as pg
import time


class Arena():
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def GiveBaff(self, pokemon):
        pokemon.health += 10

    def PrintINFO(self, Team1, Team2):
        print("________________________")
        print('Команда 2го игрока:')
        Team1.Pokemons[0].INFO()
        print('_______')
        Team1.Pokemons[1].INFO()
        print('_______')
        Team1.Pokemons[2].INFO()
        print("________________________")
        print('Команда 1го игрока:')
        print("________________________")
        Team2.Pokemons[0].INFO()
        print('_______')
        Team2.Pokemons[1].INFO()
        print('_______')
        Team2.Pokemons[2].INFO()
        print("________________________")

    def MakeTeams(self, player1team, player2team):
        pg.init()
        pg.mixer.music.load('MainTheme.mp3')
        pg.mixer.music.play()

        for j in range(1, 3):
            print("________________________")
            print(f"Игрок {j}, выбирайте тренера")
            for i in range(len(mastersstats)):
                print(f'{i + 1})')
                print(mastersstats[i].name)
            k = int(input())
            if (j == 1):
                player1team.append(mastersstats[k - 1])
            else:
                player2team.append(mastersstats[k - 1])
            mastersstats.remove(mastersstats[k - 1])

        for j in range(1, 3):
            print("________________________")
            print(f"Игрок {j}, выбирайте доктора")
            for i in range(len(doctorsstats)):
                print(f'{i + 1})')
                print(doctorsstats[i].name)
            k = int(input())
            if (j == 1):
                player1team.append(doctorsstats[k - 1])
            else:
                player2team.append(doctorsstats[k - 1])
            doctorsstats.remove(doctorsstats[k - 1])

        for j in range(1, 3):
            print("________________________")
            print(f"Игрок {j}, выбирайте наблюдателя")
            for i in range(len(spectatorsstats)):
                print(f'{i + 1})')
                print(spectatorsstats[i].name)
            k = int(input())
            if (j == 1):
                player1team.append(spectatorsstats[k - 1])
            else:
                player2team.append(spectatorsstats[k - 1])
            spectatorsstats.remove(spectatorsstats[k - 1])

        pokemons1 = []
        pokemons2 = []

        for i in range(3):
            for j in range(1, 3):
                print("________________________")
                print(f"Игрок {j}, выбирайте покемончика")
                for i in range(len(pokemonsstats)):
                    print(f'{i + 1})')
                    print(pokemonsstats[i].name)
                k = int(input())
                if (j == 1):
                    pokemons1.append(pokemonsstats[k - 1])
                else:
                    pokemons2.append(pokemonsstats[k - 1])
                pokemonsstats.remove(pokemonsstats[k - 1])

        Teams = []
        Team1 = Team(player2team[0], player2team[1], player2team[2], pokemons2)
        Team2 = Team(player1team[0], player1team[1], player1team[2], pokemons1)
        Teams.append(Team1)
        Teams.append(Team2)
        pg.mixer.music.pause()
        return Teams

    def Fight(self, Team1, Team2):
        if (self.name == 'на Чёрной горе'):
            pg.mixer.music.load('Inferno.mp3')
            pg.mixer.music.play()
        if (self.name == 'в бухте Черносерда'):
            pg.mixer.music.load('Boloto.mp3')
            pg.mixer.music.play()
        if (self.name == 'на Альтеракском перевале'):
            pg.mixer.music.load('Stronghold.mp3')
            pg.mixer.music.play()
        if (self.name == 'в городе Жуковский, Гагарина 16'):
            pg.mixer.music.load('Tower.mp3')
            pg.mixer.music.play()

        print(f'Небеса разверзлись и обе команды затянуло в неопознанную дыру')
        print(f'Когда герои очнулись, то поняли, что находятся {self.name}')
        print('Первыми на махач выходят:')
        print(f'{Team1.Pokemons[0].name} со стороны 2ой команды')
        print(f'{Team2.Pokemons[0].name} со стороны 1ой команды')
        for i in range(3):
            Team1.Pokemons[i].armor += Team1.Master.intelligence
            Team1.Pokemons[i].health += Team1.Master.stamina
            Team2.Pokemons[i].armor += Team2.Master.intelligence
            Team2.Pokemons[i].health += Team2.Master.stamina
        Teams = []
        Teams.append(Team1)
        Teams.append(Team2)
        fighters = []
        fighters.append(Team1.Pokemons[0])
        fighters.append(Team2.Pokemons[0])
        while (((Team1.Pokemons[0].health > 0) or (Team1.Pokemons[1].health > 0) or (Team1.Pokemons[2].health > 0)) and ((Team2.Pokemons[0].health > 0) or (Team2.Pokemons[1].health > 0) or (Team2.Pokemons[2].health > 0))):
            print("________________________")
            for tr in range(2):
                print("________________________")
                if (tr == 0):
                    print(f'Наступает ход {tr+2}го игрока')
                    forprint = tr + 2
                else:
                    print(f'Наступает ход {tr}го игрока')
                    forprint = tr

                self.PrintINFO(Team1, Team2)

                print('1 фаза хода')
                if (Teams[tr].Doctor.usages > 0) or (Teams[tr].Spectator.usages > 0):
                    print("________________________")
                    print(f'У вас {Teams[tr].Doctor.usages} ходов для доктора')
                    if (Teams[tr].Doctor.usages == 0):
                        print('Вы не можете ходить доктором')
                    print(f'{Teams[tr].Spectator.usages} ходов для наблюдателя')
                    if (Teams[tr].Spectator.usages == 0):
                        print('Вы не можете ходить наблюдателем')
                    print('Кем хотите походить: доктором(1),наблюдателем(2) или пропустить ход(3)?')
                    playerturn = int(input())
                    if (playerturn == 1) and (Teams[tr].Doctor.usages > 0):
                        print("________________________")
                        Teams[tr].Doctor.HealPokemon(fighters[tr])
                        print(
                            f'Доктор {Teams[tr].Doctor.name} вставил шприц {fighters[tr].name} по самые гланды и излечил того на {Teams[tr].Doctor.healstrength}')
                        Teams[tr].Doctor.usages -= 1
                    elif (playerturn == 1):
                        print("________________________")
                        print('Вы не можете походить доктором, но можете походить наблюдателем')
                        print("________________________")
                        print('Хожу наблюдателем(1)')
                        print('Пропускаю ход(2)')
                        playerturn1 = int(input())
                        print("________________________")
                        if (playerturn1 == 1):
                            print('Поддержать(1) или обосрать(2)?')
                            choice = int(input())
                            if (choice == 1):
                                Teams[tr].Spectator.Сheerup(fighters[tr])
                                print(f'{Teams[tr].Spectator.name} прокричал "Используй силу" и {fighters[tr].name} использовал силу(получил {Teams[tr] .Spectator.support} к атаке)')
                                Teams[tr].Spectator.usages -= 1
                            if (choice == 2):
                                Teams[tr].Spectator.Boo(fighters[len(fighters)-tr-1])
                                print(f'{Teams[tr].Spectator.name} прокричал "ЛЕЖАТЬ + СОСАТЬ" и {fighters[len(fighters)-tr-1].name} расстроился(получил -{Teams[tr].Spectator.support} к атаке)')
                                Teams[tr].Spectator.usages -= 1
                    if (playerturn == 2) and (Teams[tr].Spectator.usages > 0):
                        print("________________________")
                        print('Поддержать(1) или обосрать(2)?')
                        choice = int(input())
                        if (choice == 1):
                            Teams[tr].Spectator.Сheerup(fighters[tr])
                            print(f'{Teams[tr].Spectator.name} прокричал "Используй силу" и {fighters[tr].name} использовал силу(получил {Teams[tr].Spectator.support} к атаке)')
                            Teams[tr].Spectator.usages -= 1
                        if (choice == 2):
                            Team1.Spectator.Boo(fighters[len(fighters)-tr-1])
                            print(f'{Teams[tr].Spectator.name} прокричал "ЛЕЖАТЬ + СОСАТЬ" и {fighters[len(fighters)-tr-1].name} расстроился(получил -{Teams[tr].Spectator.support} к атаке)')
                            Teams[tr].Spectator.usages -= 1
                    elif (playerturn == 2):
                        print("________________________")
                        print('Вы не можете походить наблюдателем, но можете походить доктором')
                        print("________________________")
                        print('Хожу доктором(1)')
                        print('Пропускаю ход(2)')
                        playerturn1 = int(input())
                        print("________________________")
                        if (playerturn1 == 1):
                            print("________________________")
                            Teams[tr].Doctor.HealPokemon(fighters[tr])
                            print(f'Доктор {Teams[tr].Doctor.name} вставил шприц {fighters[tr].name} по самые гланды и излечил того на {Teams[tr].Doctor.healstrength}')
                            Teams[tr].Doctor.usages -= 1
                    if (playerturn == 3):
                        print('Пропуск действия,переход ко 2ой фазе хода')
                if (Teams[tr].Doctor.usages == 0) and (Teams[tr].Spectator.usages == 0):
                    print("________________________")
                    print('Вы больше не можете использовать способности людей,переход ко 2ой фазе хода')


                for i in range(3):
                    Teams[tr].Pokemons[i].cdtek1 -= 1
                    if (Teams[tr].Pokemons[i].cdtek1 < 0):
                        Teams[tr].Pokemons[i].cdtek1 = 0

                    Teams[tr].Pokemons[i].cdtek2 -= 1
                    if (Teams[tr].Pokemons[i].cdtek2 < 0):
                        Teams[tr].Pokemons[i].cdtek2 = 0

                print('2 фаза хода')
                self.PrintINFO(Team1, Team2)

                print("________________________")
                print('Выберите действие:')
                print('1)НыыыА(Дать тычку)')
                if (fighters[tr].cdtek1 == 0):
                    print('2)НыыЫЫЫАА(использовать классовую способность)')
                if (fighters[tr].cdtek2 == 0):
                    print('3)НННЫЫЫЫЫЫЫЫЫЫЫЫАААААААА(использовать уникальную способность)')
                print('4) НЫА отменяется(поменять текущего бойца с покемоном со скамьи запасных)')
                choice = int(input())

                if (choice == 1):
                    fighters[len(fighters)-tr-1].health -= fighters[tr].damage - fighters[len(fighters)-tr-1].armor
                    print("________________________")
                    print(f'"Получай по щам"-слышится с трибуны ({fighters[len(fighters)-tr-1].name} получил {fighters[tr].damage}-{fighters[len(fighters)-tr-1].armor} урона)')
                    if ((Teams[len(Teams)-tr-1].Pokemons[0].health <= 0) and (Teams[len(Teams)-tr-1].Pokemons[1].health <= 0) and (Teams[len(Teams)-tr-1].Pokemons[2].health <= 0)):
                        print("________________________")
                        print(f'Игрок {forprint} влёгкую размазал соперника и вырвал сердце из его груди')
                        break
                    if (fighters[len(fighters)-tr-1].health < 0):
                        print("________________________")
                        print(f'Погиб {fighters[len(fighters)-tr-1].name} - невольник чести -')
                        print('Пал, оклеветанный молвой,')
                        print('С свинцом в груди и жаждой мести,')
                        print('Поникнув гордой головой!')
                        for i in range(3):
                            if (Teams[len(Teams) - tr - 1].Pokemons[i].health > 0):
                                fighters[len(fighters)-tr-1] = Teams[len(Teams)-tr-1].Pokemons[i]
                        print(f'На замену собрату выходит другой гений:{fighters[len(fighters)-tr-1].name}')

                if (choice == 2) and (fighters[tr].cdtek1 == 0):
                    fighters[tr].Special_fight(fighters[len(fighters)-tr-1])
                    fighters[tr].cdtek1 = fighters[tr].cd1
                    if ((Teams[len(Teams) - tr - 1].Pokemons[0].health <= 0) and (Teams[len(Teams) - tr - 1].Pokemons[1].health <= 0) and (Teams[len(Teams) - tr - 1].Pokemons[2].health <= 0)):
                        print("________________________")
                        print(f'Игрок {forprint} влёгкую размазал соперника и вырвал сердце из его груди')
                        break
                    if (fighters[len(fighters) - tr - 1].health < 0):
                        print("________________________")
                        print(f'Погиб {fighters[len(fighters) - tr - 1].name} - невольник чести -')
                        print('Пал, оклеветанный молвой,')
                        print('С свинцом в груди и жаждой мести,')
                        print('Поникнув гордой головой!')
                        for i in range(3):
                            if (Teams[len(Teams) - tr - 1].Pokemons[i].health > 0):
                                fighters[len(fighters) - tr - 1] = Teams[len(Teams) - tr - 1].Pokemons[i]
                        print(f'На замену собрату выходит другой гений:{fighters[len(fighters) - tr - 1].name}')
                elif (choice == 2):
                    print('Ты безуспешно попытался обхитрить систему, ход пропущен')

                if (choice == 3) and (fighters[tr].cdtek2 == 0):
                    print('________________________')
                    if (fighters[tr].numoftargets == 1):
                        fighters[tr].Personal_Ability(fighters[len(fighters) - tr - 1])
                    if (fighters[tr].numoftargets == -1):
                        fighters[tr].Personal_Ability()
                    if (fighters[tr].numoftargets == 0):
                        a = []
                        for i in range(3):
                            if ((fighters[tr].health != Teams[tr].Pokemons[i].health) or (fighters[tr].damage != Teams[tr].Pokemons[i].damage) or (fighters[tr].armor != Teams[tr].Pokemons[i].armor)):
                                a.append(Teams[tr].Pokemons[i])
                        fighters[tr].Personal_Ability(a)
                    if (fighters[tr].numoftargets > 1):
                        b = []
                        if (fighters[tr].name == 'Morphling'):
                            b.append(fighters[len(fighters) - tr - 1])
                        for i in range(3):
                            b.append(Teams[len(Teams) - tr - 1].Pokemons[i])
                        fighters[tr].Personal_Ability(b)
                    fighters[tr].cdtek2 = fighters[tr].cd2
                    if ((Teams[len(Teams) - tr - 1].Pokemons[0].health <= 0) and (Teams[len(Teams) - tr - 1].Pokemons[1].health <= 0) and (Teams[len(Teams) - tr - 1].Pokemons[2].health <= 0)):
                        print("________________________")
                        print(f'Игрок {forprint} влёгкую размазал соперника и вырвал сердце из его груди')
                        break
                    if (fighters[len(fighters) - tr - 1].health < 0):
                        print("________________________")
                        print(f'Погиб {fighters[len(fighters) - tr - 1].name} - невольник чести -')
                        print('Пал, оклеветанный молвой,')
                        print('С свинцом в груди и жаждой мести,')
                        print('Поникнув гордой головой!')
                        for i in range(3):
                            if (Teams[len(Teams) - tr - 1].Pokemons[i].health > 0):
                                fighters[len(fighters) - tr - 1] = Teams[len(Teams) - tr - 1].Pokemons[i]
                        print(f'На замену собрату выходит другой гений:{fighters[len(fighters) - tr - 1].name}')
                elif (choice == 3):
                    print('Ты безуспешно попытался обхитрить систему, ход пропущен')

                if (choice == 4):
                    print("________________________")
                    print('На кого хотите заменить?')
                    if (fighters[tr] != Teams[tr].Pokemons[0]):
                        print(f'1){Teams[tr].Pokemons[0].name}')
                    if (fighters[tr] != Teams[tr].Pokemons[1]):
                        print(f'2){Teams[tr].Pokemons[1].name}')
                    if (fighters[tr] != Teams[tr].Pokemons[2]):
                        print(f'3){Teams[tr].Pokemons[2].name}')
                    playerchoice = int(input())
                    if (playerchoice == 1) and (Teams[tr].Pokemons[0].health > 0):
                        fighters[tr] = Teams[tr].Pokemons[0]
                    elif (playerchoice == 1):
                        print('Чё, думал самый умный? Ты не заменишь дешёвкой своего покемона и он умрёт мучительной смертью')
                    if (playerchoice == 2) and (Teams[tr].Pokemons[1].health > 0):
                        fighters[tr] = Teams[tr].Pokemons[1]
                    elif (playerchoice == 2):
                        print('Чё, думал самый умный? Ты не заменишь дешёвкой своего покемона и он умрёт мучительной смертью')
                    if (playerchoice == 3) and (Team1.Pokemons[1].health > 0):
                        fighters[tr] = Teams[tr].Pokemons[2]
                    elif (playerchoice == 3):
                        print('Чё, думал самый умный? Ты не заменишь дешёвкой своего покемона и он умрёт мучительной смертью')


            bonus = random.randrange(1, 2, 1)
            if (bonus == 1):
                self.GiveBaff(fighters[tr])
                print("________________________")
                print(f'{fighters[tr].name} получил бонус {self.name}')
            if (bonus == 2):
                self.GiveBaff(fighters[len(fighters) - tr - 1])
                print("________________________")
                print(f'{fighters[len(fighters) - tr - 1].name} получил бонус {self.name}')


class WaterArena(Arena):
    def GiveBaff(self, pokemon):
        pokemon.health += 10


class FireArena(Arena):
    def GiveBaff(self, pokemon):
        pokemon.health -= 10


class EarthArena(Arena):
    def GiveBaff(self, pokemon):
        pokemon.armor += 3


class FALTArena(Arena):
    def GiveBaff(self, pokemon):
        pokemon.damage += 5


Master0 = Master('MilfHunter95', 2, 10)
Master1 = Master('Hyperion', 3, 8)
Master2 = Master('X_Your_Dreams', 1, 12)
Doctor0 = Doctor('Panichishin', 60, 1)
Doctor1 = Doctor('Ded', 20, 3)
Doctor2 = Doctor('Ostapow', 30, 2)
Spectator0 = Spectator('Maxim', 6, 1)
Spectator1 = Spectator('Vadim', 3, 2)
Spectator2 = Spectator('Ilya', 2, 3)
Pokemon0 = EmberSpirit('Ember Spirit', 15, 90, 2, 3, 0, 2, 0, 90, 3)
Pokemon1 = Ragnaros('Ragnaros', 26, 70, 3, 3, 0, 5, 0, 70, 1)
Pokemon2 = Deathwing('Deathwing', 22, 80, 3, 3, 0, 4, 0, 90, 2)
Pokemon3 = Morphling('Morphling', 17, 80, 3, 3, 0, 3, 0, 80, 3)
Pokemon4 = Slardar('Slardar', 14, 90, 4, 3, 0, 3, 0, 90, 1)
Pokemon5 = Murchal('Murchal', 24, 65, 3, 3, 0, 1, 0, 65, 1)
Pokemon6 = EarthSpirit('Earth Spirit', 17, 90, 4, 3, 0, 4, 0, 90, 1)
Pokemon7 = Malfurion('Malfurion', 10, 110, 5, 3, 0, 4, 0, 110, 0)
Pokemon8 = Tiny('Tiny', 15, 100, 7, 3, 0, 4, 0, 100, -1)
Pokemon9 = StormSpirit('Storm Spirit', 19, 85, 3, 3, 0, 3, 0, 85, 3)
Pokemon10 = Grisha('Grisha', 15, 90, 5, 3, 0, 3, 0, 90, 3)
Pokemon11 = TovaristchBurmistrov('Tovaristch Burmistrov', 22, 75, 3, 3, 0, 2, 0, 75, 1)
Arena0 = FireArena('на Чёрной горе', 'огонь')
Arena1 = WaterArena('в бухте Черносерда', 'вода')
Arena2 = EarthArena('на Альтеракском перевале', 'земля')
Arena3 = FALTArena('в городе Жуковский, Гагарина 16', 'воздух')

Arenas = []
Arenas.append(Arena0)
Arenas.append(Arena1)
Arenas.append(Arena2)
Arenas.append(Arena3)

mastersstats = []
mastersstats.append(Master0)
mastersstats.append(Master1)
mastersstats.append(Master2)

doctorsstats = []
doctorsstats.append(Doctor0)
doctorsstats.append(Doctor1)
doctorsstats.append(Doctor2)

spectatorsstats = []
spectatorsstats.append(Spectator0)
spectatorsstats.append(Spectator1)
spectatorsstats.append(Spectator2)

pokemonsstats = []
pokemonsstats.append(Pokemon0)
pokemonsstats.append(Pokemon1)
pokemonsstats.append(Pokemon2)
pokemonsstats.append(Pokemon3)
pokemonsstats.append(Pokemon4)
pokemonsstats.append(Pokemon5)
pokemonsstats.append(Pokemon6)
pokemonsstats.append(Pokemon7)
pokemonsstats.append(Pokemon8)
pokemonsstats.append(Pokemon9)
pokemonsstats.append(Pokemon10)
pokemonsstats.append(Pokemon11)
