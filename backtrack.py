import math
import copy
from eliminate import importsud





def backtrack(board,success=[],lasti=-1,lasty=-1):
    
    for i in range(9):
        for y in range(9):
            if isinstance(board[i][y],list):
                for num in range(1,10):
                    
                    if legalcheck(board,i,y,num):
                        board[i][y]=num
                        board=backtrack(board,success,i,y)
                        if len(board)<9:
                            print("whoops",board)
                        if not isinstance(board[i][y],list):
                            return board
                        
                #print(board)
                if lasti>-1:
                    board[lasti][lasty]=[]
                    for x in range(1,len(board)+1):
                        board[lasti][lasty].append(x)
                return board

    print("hurray")
  
    
    #print(success[0])
    return board


def checkamo(board,success=[],lasti=-1,lasty=-1):
    
    for i in range(9):
        for y in range(9):
            if isinstance(board[i][y],list):
                for num in range(1,10):
                    
                    if legalcheck(board,i,y,num):
                        board[i][y]=num
                        [board,success]=checkamo(board,success,i,y,)
                        #if not isinstance(board[i][y],list):
                         #   return board
                        if len(success)>1:
                            return [board,success]
                #print(board)
                if lasti>-1:
                    board[lasti][lasty]=[]
                    for x in range(1,len(board)+1):
                        board[lasti][lasty].append(x)
                return [board,success]


    
    #print("hurrayyy")
    success.append(copy.copy(board))
    #print("solution: ",success)
    board[lasti][lasty]=[]
    for x in range(1,len(board)+1):
        board[lasti][lasty].append(x)
    #print(success[0])
    return [board,success]

def checksol2(board,success=0,lasti=0,lasty=0):
    
    for i in range(9):
        for y in range(9):
            if isinstance(board[i][y],list):
                for num in range(1,10):
                    
                    if legalcheck(board,i,y,num):
                        board[i][y]=num
                        [board,success]=checksol2(board,success,i,y,)
                        #if not isinstance(board[i][y],list):
                         #   return board
                        
                        if success>2:
                            print("done")
                            return [board,success]
                #print(board)
                if lasti>-1:
                    board[lasti][lasty]=[]
                    for x in range(1,len(board)+1):
                        board[lasti][lasty].append(x)
                return [board,success]

    print("hurray", lasti,lasty,i,y)
    success+=1
    board[lasti][lasty]=[]
    for x in range(1,len(board)+1):
        board[lasti][lasty].append(x)
    #print(success[0])
    return [board,success]

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
            if board[smallrow][smallcol] in range(1,10):
                if board[smallrow][smallcol]==num:# and len(board[row][col])>1:# and isinstance(board[row][i],int):
                    #print(board[smallrow][smallcol]) #just temphere
                    return False
    
    return True

def  checksolve(board):

    size=len(board)

    for i in range(size):
        for y in range(size):
            num=board[i][y]
            board[i][y]=list(range(1,size+1))
            if legalcheck(board,i,y,num):
                return True
            board[i][y]=num
    return False

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

finish="no"
#finish=backtrack(importsud(primeeas))

for i in range(9):
    if isinstance(finish,list):
        print(finish[i])
