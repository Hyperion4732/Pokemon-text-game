turn = 1

while (turn == 1):
    print("________________________")
    print('Наступает ход 1го игрока')

    self.PrintINFO(Team1, Team2)

    print('1 фаза хода')
    if (Team2.Doctor.usages > 0) or (Team2.Spectator.usages > 0):
        print("________________________")
        print(f'У вас {Team2.Doctor.usages} ходов для доктора')
        if (Team2.Doctor.usages == 0):
            print('Вы не можете ходить доктором')
        print(f'{Team2.Spectator.usages} ходов для наблюдателя')
        if (Team2.Spectator.usages == 0):
            print('Вы не можете ходить наблюдателем')
        print('Кем хотите походить: доктором(1),наблюдателем(2) или пропустить ход(3)?')
        playerturn = int(input())
        if (playerturn == 1) and (Team2.Doctor.usages > 0):
            print("________________________")
            Team2.Doctor.HealPokemon(fighter1)
            print(
                f'Доктор {Team2.Doctor.name} вставил шприц {fighter2.name} по самые гланды и излечил того на {Team2.Doctor.healstrength}')
            Team2.Doctor.usages -= 1
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
                    Team2.Spectator.Сheerup(fighter2)
                    print(f'{Team2.Spectator.name} прокричал "Используй силу" и {fighter2.name} использовал силу(получил {Team2.Spectator.support} к атаке)')
                    Team2.Spectator.usages -= 1
                if (choice == 2):
                    Team2.Spectator.Boo(fighter2)
                    print(f'{Team2.Spectator.name} прокричал "ЛЕЖАТЬ + СОСАТЬ" и {fighter1.name} расстроился(получил -{Team2.Spectator.support} к атаке)')
                    Team2.Spectator.usages -= 1
        if (playerturn == 2) and (Team2.Spectator.usages > 0):
            print("________________________")
            print('Поддержать(1) или обосрать(2)?')
            choice = int(input())
            if (choice == 1):
                Team2.Spectator.Сheerup(fighter1)
                print(f'{Team2.Spectator.name} прокричал "Используй силу" и {fighter2.name} использовал силу(получил {Team2.Spectator.support} к атаке)')
                Team1.Spectator.usages -= 1
            if (choice == 2):
                Team2.Spectator.Boo(fighter2)
                print(f'{Team2.Spectator.name} прокричал "ЛЕЖАТЬ + СОСАТЬ" и {fighter1.name} расстроился(получил -{Team2.Spectator.support} к атаке)')
                Team2.Spectator.usages -= 1
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
                Team2.Doctor.HealPokemon(fighter2)
                print(f'Доктор {Team2.Doctor.name} вставил шприц {fighter2.name} по самые гланды и излечил того на {Team2.Doctor.healstrength}')
                Team2.Doctor.usages -= 1
        if (playerturn == 3):
            print('Пропуск действия,переход ко 2ой фазе хода')
    if (Team2.Doctor.usages == 0) and (Team2.Spectator.usages == 0):
        print("________________________")
        print('Вы больше не можете использовать способности людей,переход ко 2ой фазе хода')

    print('2 фаза хода')

    Team2.Pokemons[0].cdtek1 -= 1
    if (Team2.Pokemons[0].cdtek1 < 0):
        Team2.Pokemons[0].cdtek1 = 0

    Team2.Pokemons[0].cdtek2 -= 1
    if (Team2.Pokemons[0].cdtek2 < 0):
        Team2.Pokemons[0].cdtek2 = 0

    Team2.Pokemons[1].cdtek1 -= 1
    if (Team2.Pokemons[1].cdtek1 < 0):
        Team2.Pokemons[1].cdtek1 = 0

    Team2.Pokemons[1].cdtek2 -= 1
    if (Team2.Pokemons[1].cdtek2 < 0):
        Team2.Pokemons[1].cdtek2 = 0

    Team2.Pokemons[2].cdtek1 -= 1
    if (Team2.Pokemons[2].cdtek1 < 0):
        Team2.Pokemons[2].cdtek1 = 0

    Team2.Pokemons[2].cdtek2 -= 1
    if (Team2.Pokemons[2].cdtek2 < 0):
        Team2.Pokemons[2].cdtek2 = 0

    self.PrintINFO(Team1, Team2)

    print("________________________")
    print('Выберите действие:')
    print('1)НыыыА(Дать тычку)')
    if (fighter2.cdtek1 == 0):
        print('2)НыыЫЫЫАА(использовать классовую способность)')
    if (fighter2.cdtek2 == 0):
        print('3)НННЫЫЫЫЫЫЫЫЫЫЫЫАААААААА(использовать уникальную способность)')
    print('4) НЫА отменяется(поменять текущего бойца с покемоном со скамьи запасных)')
    choice = int(input())

    if (choice == 1):
        fighter1.health -= fighter2.damage - fighter1.armor
        print("________________________")
        print(f'"Получай по щам"-слышится с трибуны({fighter1.name} получил {fighter2.damage}-{fighter1.armor} урона)')
        if ((Team1.Pokemons[0].health <= 0) and (Team1.Pokemons[1].health <= 0) and (Team1.Pokemons[0].health <= 0)):
            print("________________________")
            print('Игрок 1 влёгкую размазал соперника и вырвал сердце из его груди')
            break
        if (fighter1.health <= 0):
            print("________________________")
            print(f'Погиб {fighter1.name} - невольник чести -')
            print('Пал, оклеветанный молвой,')
            print('С свинцом в груди и жаждой мести,')
            print('Поникнув гордой головой!')
            for i in range(3):
                if (Team1.Pokemons[i].health > 0):
                    fighter1 = Team1.Pokemons[i]
            print(f'На замену собрату выходит другой гений:{fighter1.name}')

    if (choice == 2) and (fighter2.cdtek1 == 0):
        fighter2.Special_fight(fighter1)
        fighter2.cdtek1 = fighter2.cd1
        if ((Team1.Pokemons[0].health <= 0) and (Team1.Pokemons[1].health <= 0) and (Team1.Pokemons[0].health <= 0)):
            print("________________________")
            print('Игрок 1 влёгкую размазал соперника и вырвал сердце из его груди')
            break
        if (fighter2.health <= 0):
            print("________________________")
            print(f'Погиб {fighter1.name} - невольник чести -')
            print('Пал, оклеветанный молвой,')
            print('С свинцом в груди и жаждой мести,')
            print('Поникнув гордой головой!')
            for i in range(3):
                if (Team1.Pokemons[i].health > 0):
                    fighter1 = Team1.Pokemons[i]
            print(f'На замену собрату выходит другой гений:{fighter1.name}')
    elif (choice == 2):
        print('Ты безуспешно попытался обхитрить систему, ход пропущен')

    if (choice == 3) and (fighter2.cdtek2 == 0):
        print('________________________')
        if (fighter2.numoftargets == 1):
            fighter2.Personal_Ability(fighter1)
        if (fighter2.numoftargets == -1):
            fighter2.Personal_Ability()
        if (fighter2.numoftargets == 0):
            a = []
            for i in range(3):
                if ((fighter2.health != Team2.Pokemons[i].health) or (fighter2.damage != Team2.Pokemons[i].damage) or (fighter2.armor != Team2.Pokemons[i].armor)):
                    a.append(Team2.Pokemons[i])
            fighter2.Personal_Ability(a)
        if (fighter2.numoftargets > 1):
            b = []
            if (fighter2.name == 'Morphling'):
                b.append(fighter1)
            for i in range(3):
                b.append(Team1.Pokemons[i])
            fighter2.Personal_Ability(b)
        fighter2.cdtek2 = fighter2.cd2
        if ((Team1.Pokemons[0].health <= 0) and (Team1.Pokemons[1].health <= 0) and (Team1.Pokemons[0].health <= 0)):
            print("________________________")
            print('Игрок 1 влёгкую размазал соперника и вырвал сердце из его груди')
            break
        if (fighter1.health <= 0):
            print("________________________")
            print(f'Погиб {fighter1.name} - невольник чести -')
            print('Пал, оклеветанный молвой,')
            print('С свинцом в груди и жаждой мести,')
            print('Поникнув гордой головой!')
            for i in range(3):
                if (Team1.Pokemons[i].health > 0):
                    fighter1 = Team1.Pokemons[i]
            print(f'На замену собрату выходит другой гений:{fighter1.name}')
    elif (choice == 3):
        print('Ты безуспешно попытался обхитрить систему, ход пропущен')

    if (choice == 4):
        print("________________________")
        print('На кого хотите заменить?')
        if (fighter2 != Team2.Pokemons[0]):
            print(f'1){Team2.Pokemons[0].name}')
        if (fighter2 != Team2.Pokemons[1]):
            print(f'2){Team2.Pokemons[1].name}')
        if (fighter2 != Team2.Pokemons[2]):
            print(f'3){Team2.Pokemons[2].name}')
        playerchoice = int(input())
        if (playerchoice == 1) and (Team2.Pokemons[0].health > 0):
            fighter2 = Team2.Pokemons[0]
        elif (playerchoice == 1):
            print('Чё, думал самый умный? Ты не заменишь дешёвкой своего покемона и он умрёт мучительной смертью')
        if (playerchoice == 2) and (Team2.Pokemons[1].health > 0):
            fighter2 = Team2.Pokemons[1]
        elif (playerchoice == 2):
            print('Чё, думал самый умный? Ты не заменишь дешёвкой своего покемона и он умрёт мучительной смертью')
        if (playerchoice == 3) and (Team2.Pokemons[1].health > 0):
            fighter2 = Team2.Pokemons[2]
        elif (playerchoice == 3):
            print('Чё, думал самый умный? Ты не заменишь дешёвкой своего покемона и он умрёт мучительной смертью')

    turn = 0