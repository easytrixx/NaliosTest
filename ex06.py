def turn(game, symbol):
    i=0;
    winner=False
    winnerName=""
    if isNoneInMatrix(game)==False or winner:
        return "Game is Over ",winnerName, "win !"

    a, b = input("Enter where you want to place: ", symbol).split()
    while game[a][b] is not None:
        a, b = input("Enter where you want to place: ",symbol).split()


    game[a][b]=symbol



    return game;

def isNoneInMatrix(game):

    for i in matrix:
        for j in matrix[0]:
            if matrix[i][j] is None:
                return True;
    return False;



if __name__ == "__main__":

    matrix=([None,None,None],[None,None,None],[None,None,None])
    turn()

# Pour la suite, je voulais tester si un joueur avait gagné la partie. Si c'est le cas, on retourne la matrice et on finit la partie, sinon elle continue jusqu'à ce qu'il y ait un gagnant ou que la grille est remplie (aucun vainqueur)