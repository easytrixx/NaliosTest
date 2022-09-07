
def game_of_life(matrix,nbIter):
    for k in range(nbIter):
        newmatrix = [([0] * len(matrix[0])) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                neighbours = []
                for row in range(-1,2):
                    if i+row>=0 and i+row<len(matrix):
                        for col in range(-1, 2):
                            if j+col >= 0 and j+col < len(matrix[0]):
                                if row==0 and col==0:
                                    continue
                                neighbours.append(matrix[row+i][col+j])
                neighbours_alive=neighbours.count(1)
                print(matrix[i][j], " " ,neighbours_alive)
                if neighbours_alive<=1 or neighbours_alive>=4:
                    newmatrix[i][j]=0
                elif neighbours_alive==3:
                    newmatrix[i][j]=1
                else:
                    newmatrix[i][j]=matrix[i][j]
        matrix = newmatrix

    return newmatrix



if __name__ == "__main__":
    matrix = game_of_life(([0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]),5)
    print(matrix)

