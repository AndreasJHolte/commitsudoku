import math
import copy
from create2 import *
from eliminate import *
from backtrack import *
from interface import *
import random




def randomseed(size=3,min=21,max=40):

    board=createboard(size)

    seed=random.randint(min,max)
    i=0
    while i<seed:


        row=random.randint(0,size*size-1)
        col=random.randint(0,size*size-1)
        num=random.randint(1,size*size)
   
        if isinstance(board[row][col],list):
           
            if legalcheck(board,row,col,num):
                board[row][col]=num
                i+=1
    return board

def findunique(size=3,difficulty=1,mode="rain"):
    if mode=="random":
        attempt=1
        while True:
            print("attempt: ",attempt)
            seed=randomseed(size,25,27)
            if checksud(seed)==1:
                return seed
            attempt+=1
    elif mode=="rain":

        seed=backtrack(randomseed(size,14,15))
        if difficulty==1:
            divide=2.0
        elif difficulty==2:
            divide=2.5
        elif difficulty==3:
            divide=3.0
        knowns=size*size*size*size
        treshold=size*size*size*size/divide
        while knowns>treshold:
            oldseed=copy.copy(seed)
            knowns=0
            for i in range(10):
                row=random.randint(0,size*size-1)
                col=random.randint(0,size*size-1)

                seed[row][col]=list(range(size*size))

            if checksud(seed)!=1:
                seed=oldseed

            for i in range(size*size):
                for y in range(size*size):
                    if isinstance(seed[i][y],int):
                        knowns+=1
        return seed
        

def checksud(board): #does not work twice on the same board? record the answer the first time

    return len(checkamo(copy.copy(board),[])[1])
    
primeeasy=[[0,3,0,7,0,0,0,0,0],
               [0,0,2,0,0,0,6,0,0],
               [8,0,0,0,1,3,0,0,5],
               [0,6,0,0,7,4,5,0,0],
               [4,0,0,9,0,0,0,0,0],
               [0,0,0,8,0,0,0,0,7],
               [0,0,0,0,0,9,0,0,0],
               [3,0,0,0,4,5,0,0,1],
               [0,8,0,0,0,0,0,3,0]]

maybe=[[2, 3, 4, 1, 5, 6, 7, 8, 9], [1, 5, 6, 7, 9, 8, 2, 3, 4], [7, 8, 9, 2, 3, 4, 1, 5, 6], [3, 1, 2, 4, 6, 5, 8, 9, 7], [4, 7, 5, 9, 8, 1, 6, 2, 3], [6, 9, 8, 3, 2, 7, 4, 1, 5], [8, 2, 7, 5, 4, 9, 3, 6, 1], [5, 4, 
3, 6, 1, 2, 9, 7, 8], [9, 6, 1, 8, 7, 3, 5, 4, 2]]

#tryhard=randomseed()
#tryhard=createboard(3)
#[tryhard,suc]=backtrack(importsud(primeeasy))
suc=findunique()


displaycompact(suc)
displaycompact(backtrack(suc))






#print(backtrack(tryhard)[1][0])







