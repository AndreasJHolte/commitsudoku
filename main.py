


def createboard(size):
    board=[]
    for line in range(0,size):
        board.append([])
        for col in range(0,size):
            board[line].append([])
            for subline in range(0,size):
                board[line][col].append([])
                for subcol in range (0,size):
                    board[line][col][subline].append([])
                    for num in range(1,size*size+1):
                        board[line][col][subline][subcol].append(num)


    return board

check=createboard(2)
print(check[0][0])




