import random
def turn(game, symbol):
    a = random.randint(0,2)
    b = random.randint(0,2)
    while game[a][b]!=".":
        a = random.randint(0, 2)
        b = random.randint(0, 2)
    game[a][b]=symbol
    return game