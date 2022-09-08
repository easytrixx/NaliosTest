import random
def turn(game, symbol):
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    while game[a][b]!=".":
        a = random.randint(1, 3)
        b = random.randint(1, 3)
    game[a][b]==symbol



