


def createboard(size):
    board=[]
    for line in range(0,size*size):
        board.append([])
        for col in range(0,size*size):
            board[line].append([])
            for num in range(1,size*size+1):
                board[line][col].append(num)


    return board


check=createboard(3)
print(check[0][0])





