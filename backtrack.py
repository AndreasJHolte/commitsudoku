import math






def backtrack(board,lasti=0,lasty=0,level=0):
    
    for i in range(9):
        for y in range(9):
            if board[i][y]==0:
                for num in range(1,10):
                    
                    if legalcheck(board,i,y,num):
                        board[i][y]=num
                        board=backtrack(board,i,y,level+1)
                        if board[i][y]!=0:
                            return board
                #print(board)
                board[lasti][lasty]=0
                return board

    return board

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

finish=backtrack(primeeasy,0,0,1)

for i in range(9):
    if isinstance(finish,list):
        print(finish[i])
    else:
        print("nah")
