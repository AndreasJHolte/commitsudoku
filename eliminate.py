from create2 import *
import math
import copy


def importsud():

    board=createboard(3)

    primeeasy=[[0,3,0,7,0,0,0,0,0],
               [0,0,2,0,0,0,6,0,0],
               [8,0,0,0,1,3,0,0,5],
               [0,6,0,0,7,4,5,0,0],
               [4,0,0,9,0,0,0,0,0],
               [0,0,0,8,0,0,0,0,7],
               [0,0,0,0,0,9,0,0,0],
               [3,0,0,0,4,5,0,0,1],
               [0,8,0,0,0,0,0,3,0]]
    
    
    
    primeeas=[[0,0,0,0,0,0,5,0,1],
             [5,6,0,0,0,0,0,0,0],
             [0,0,7,2,0,4,0,0,0],
             [0,0,5,0,7,9,2,1,3],
             [0,0,4,1,0,2,0,5,9],
             [2,0,0,0,0,8,4,0,0],
             [0,0,0,3,0,5,0,0,7],
             [8,0,1,0,2,6,9,3,4],
             [0,7,3,8,9,1,0,2,5]]
    
        
    for i in range(9):
        for y in range(9):
            if primeeasy[i][y] in board[i][y]:
                board[i][y]=primeeasy[i][y]

    return board



def customsud():
    
    
    board=createboard(int(input("size:")))

    
    primeex=[[0,0,0,0,0,0,5,0,1],
             [5,6,0,0,0,0,0,0,0],
             [0,0,7,2,0,4,0,0,0],
             [0,0,5,0,7,9,2,1,3],
             [0,0,4,1,0,2,0,5,9],
             [2,0,0,0,0,8,4,0,0],
             [0,0,0,3,0,5,0,0,7],
             [8,0,1,0,2,6,9,3,4],
             [0,7,3,8,9,1,0,2,5]]
    while True:

        row=int(input("which row:"))
        col=int(input("which column:"))
        num=int(input("which number:"))

        if (10 in {row,col,num}): #fix this yeah?
            print("bye")
            return board 
        
        board[row][col]=num
        

     
def eliminate(board,lastrow=0,lastcol=0,lastcell=0):

    esc=0
    solved=True
    size=len(board)
    oldboard=board
    while solved:


        for i in range(size):
            for y in range(size):

                
                if isinstance(board[i][y],list):
                    board=checkcell(board,i,y)
                    if len(board[i][y])==1:
                        board[i][y]=board[i][y][0]
                

        solved=False
        for i in range(size):
            for y in range(size):
                if (board[i][y]) not in range(1,10):
                    
                    solved=True
                if isinstance(board[i][y],list):
                    
                    if len(board[i][y])==0:
                        print("duh ",board)
                        board[lastrow][lastcol]=lastcell
                        return board
        
        if solved==False:
            return board
        
      #  if False:
       
        esc+=1
        if esc>30:
            print("bruh")
            return board
    return board

def solve(lastboard,lastrow=0,lastcol=0,lastcell=0):

    esc=0
    board=copy.copy(lastboard)
    solved=True
    size=len(board)
    oldboard=board
    board=eliminate(lastboard)
    while solved:


        solved=False
        for i in range(size):
            for y in range(size):
                if (board[i][y]) not in range(1,10):
                    
                    solved=True
                if isinstance(board[i][y],list):
                    
                    if len(board[i][y])==10:
                        print("duh ",board)
                        
                        lastboard[lastrow][lastcol]=lastcell
                        return lastboard


        if solved==False:
            return board

        if oldboard==board:
            esc+=1
            if esc>20:
#                print("this is it:",board)
                for it in range(9):
                    for yt in range(9):
                        if isinstance(board[it][yt], list):
                            #print("list: ",board[it][yt])
                            for num in range(1,10):
                                if legalcheck(board,it,yt,num):
                                    print(num," this is list: ",board[it][yt], " and this is coords: ",it,yt )
                                    #tempboard=copy.deepcopy(board)
                                    
                                    tempcell=board[it][yt]
#                                    print("new temp: ",tempcell)
                                    board[it][yt]=num                                   
                                    #print(board)
                                    #board=eliminate(board,it,yt,tempcell)

                                    board=solve(board,it,yt,tempcell)

                                    #print("this board: ", board," and coords: ",it,yt)
                                    if board[it][yt] in range(1,10):
                                        print("yes")
                                        return board

                            lastboard[lastrow][lastcol]=lastcell
                            return lastboard
                print(board)
                print("tried")
                return board
        
        oldboard=copy.copy(board)

def legalcheck(board,row,col,num):

    if board[row][col] in range(1,10):
        return True
    size=len(board)
    bigsize=int(math.sqrt(size))
    bigrow=int((row+1)/bigsize+((row+1)%bigsize>0))-1
    if bigrow<0:
        bigrow=0
    bigcol=int((col+1)/bigsize+((col+1)%bigsize>0))-1
    if bigcol<0:
        bigcol=0

    for i in range(size):
        if board[row][i]==num:# and len(board[row][col])>1:# and isinstance(board[row][i],int):
            return False
        if board[i][col]==num:# and len(board[row][col])>1:# and isinstance(board[row][i],int):
            return False
    
    for i in range(bigsize):
        smallrow=i+3*bigrow
        for y in range(bigsize):
            smallcol=y+3*bigcol
            #print(smallcol," and ",smallrow)
            if isinstance(board[smallrow][smallcol],int):
                if board[smallrow][smallcol]==num:# and len(board[row][col])>1:# and isinstance(board[row][i],int):
                    #print(board[smallrow][smallcol]) #just temphere
                    return False
    
    return True


def checkcell(board, row, col):


    if board[row][col] in range(1,10):
        return board
    size=len(board)
    bigsize=int(math.sqrt(size))
    bigrow=int((row+1)/bigsize+((row+1)%bigsize>0))-1
    if bigrow<0:
        bigrow=0
    bigcol=int((col+1)/bigsize+((col+1)%bigsize>0))-1
    if bigcol<0:
        bigcol=0
    for i in range(size):
        if board[row][i] in board[row][col]:# and len(board[row][col])>1:# and isinstance(board[row][i],int):
            board[row][col].remove(board[row][i])
        if board[i][col] in board[row][col]:# and len(board[row][col])>1:# and isinstance(board[row][i],int):
            board[row][col].remove(board[i][col])

    for i in range(bigsize):
        smallrow=i+3*bigrow
        for y in range(bigsize):
            smallcol=y+3*bigcol
            #print(smallcol," and ",smallrow)
            if isinstance(board[smallrow][smallcol],int):
                if board[smallrow][smallcol] in board[row][col]:# and len(board[row][col])>1:# and isinstance(board[row][i],int):
                    #print(board[smallrow][smallcol]) #just temphere
                    board[row][col].remove(board[smallrow][smallcol])
    

    return board
        

#finish=backtrack(importsud(),1)
finish=solve(importsud())
print("ah")
for i in range(9):
    if isinstance(finish,list):
        print(finish[i])
    else:
        print("nah")

#importsud()

