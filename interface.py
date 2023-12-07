import math
import copy
from create2 import *
from eliminate import *






def displaylarge(board):
    

    size=len(board)
    bigsize=int(math.sqrt(size))


    
    print(" "*(bigsize+1),end="")
    print(1,end="")
    for x in range(2,size+1):
        if x<10:
            print(" "*(bigsize*2+1),end="")
            print(x,end="")
        else:
            print(" "*(bigsize*2),end="")
            print(x,end="")
    print("")

    print("|",end="")
    for x in range(size-1):
        print("-"*(bigsize*2+1),end="")
        print("+",end="")
    print("-"*(bigsize*2+1),end="")
    print("|")
    for i in range(size):

        for it in range(bigsize):
            print("|","",end="")
            for y in range(size):
            
                for yt in range(bigsize):
                    if isinstance(board[i][y],list):
                        if board[i][y][yt+it*bigsize]<10:
                            print(board[i][y][yt+it*bigsize],"",end="")
                        else:
                            print(board[i][y][yt+it*bigsize],end="")
                    elif it==1 and yt==1:
                        if board[i][y]<10:
                            print(board[i][y],"",end="")
                        else:
                            print(board[i][y],end="")
                    else:
                        print(" ","",end="")
                print("|","",end="")
            if it==1:
                print(" ",i+1,end="")
            print("")
        print("|",end="")
        for x in range(size-1):
            print("-"*(bigsize*2+1),end="")
            print("+",end="")
        print("-"*(bigsize*2+1),end="")
        print("|")


def displaycompact(board):
    size=len(board)
    bigsize=int(math.sqrt(size))

    print(" "*(2),end="")
    print(1,end="")
    for x in range(2,size+1):
        if x<10:
            print(" "*(3),end="")
            print(x,end="")
        else:
            print(" "*(2),end="")
            print(x,end="")
    print("")

    print("|",end="")
    for x in range(size-1):
        print("-"*(3),end="")
        print("+",end="")
    print("-"*(3),end="")
    print("|")

    for i in range(size):

        
        print("|","",end="")
        for y in range(size):
        
                if isinstance(board[i][y],list):
                    print(" ","",end="")
                elif board[i][y]<10:
                    print(board[i][y],"",end="")
                else:
                    print(board[i][y],end="")
                if (y+1)%bigsize==0:
                    print("|","",end="")
                else:
                    print("'","",end="")
        print(i+1)
        print("|",end="")
        for x in range(1,size):
            if (i+1)%bigsize==0:
                print("-"*(3),end="")
                print("+",end="")
            else:
                print(" - ",end="")
                print("+",end="")
        if (i+1)%bigsize==0:
            print("-"*(3),end="")
        else:
            print(" - ",end="")
    
        print("|")



def numinput(size=9):

    
    numbers=""
    for i in range(1,size+1):
        numbers=numbers+str(i)

    while True:
        num=[]
        numin=input("write in the format row column number:")
        done=True
        if len(numin)>=5:
            for i in range(3):
                if numin[i*2] in numbers:
                    print(i*2)
                    num.append(numin[i*2])
                else:
                    done=False
        else:
            done=False
        if done:
            return num
        print("wrong format, it should be like 0 0 0")


primeeasy=[[0,3,0,7,0,0,0,0,0],
               [0,0,2,0,0,0,6,0,0],
               [8,0,0,0,1,3,0,0,5],
               [0,6,0,0,7,4,5,0,0],
               [4,0,0,9,0,0,0,0,0],
               [0,0,0,8,0,0,0,0,7],
               [0,0,0,0,0,9,0,0,0],
               [3,0,0,0,4,5,0,0,1],
               [0,8,0,0,0,0,0,3,0]]

#print(numinput())

#displaylarge(importsud())

#displaycompact(randomseed(3))
#displaycompact(createboard(3))