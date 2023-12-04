from create2 import *
import math

def eliminate(board):

    return checkcell(board,1,1)



def customsud():
    
    
    board=createboard(int(input("size:")))


    while True:

        row=int(input("which row:"))
        col=int(input("which column:"))
        num=int(input("which number:"))

        if (10 in {row,col,num}): #fix this yeah?
            print("bye")
            return board 
        
        board[row][col]=num
        

     


def checkcell(board, row, col):

    size=len(board)
    bigsize=int(math.sqrt(size))
    bigrow=int(row/bigsize+(row%bigsize>0))-1
    bigcol=int(col/bigsize+(col%bigsize>0))-1
    for i in range(size):
        if board[row][i] in range(1,10):
            board[row][col].remove(board[row][i])
        if board[i][col] in range(1,10):
            board[row][col].remove(board[i][col])

    for i in range(bigsize):
        smallrow=i+1+3*bigrow
        for y in range(bigsize):
            smallcol=i+1+3*bigcol
            if board[smallrow][smallcol] in range(1,10):
                if board[smallrow][smallcol] in board[row][col]:
                    print(board[smallrow][smallcol]) #just temphere
                    board[row][col].remove(board[smallrow][smallcol])
    

    print(board[1][1])
    return board
        

print(eliminate(customsud()))


