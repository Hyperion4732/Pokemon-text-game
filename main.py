import random
from Arena import *
i = random.randrange(0, 3, 1)
FightField = Arenas[i]
player1team = []
player2team = []
Teams = []
Teams = FightField.MakeTeams(player1team, player2team)
FightField.Fight(Teams[0], Teams[1])