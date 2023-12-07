import math
import copy
import random
from solvers import *
from interface import *

def createboard(size):
    board=[]
    for line in range(0,size*size):
        board.append([])
        for col in range(0,size*size):
            board[line].append([])
            for num in range(1,size*size+1):
                board[line][col].append(num)


    return board

def importsud(board):


    size=len(board)

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
    
   

    for i in range(size):
        for y in range(size):
            if board[i][y]==0:
                board[i][y]=[]
                for x in range(size):
                    board[i][y].append(x+1)


    return board

def randomseed(size=3,min=11,max=16):

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

def findunique(size=3,lines=[],difficulty=1,mode="rain"):
    if mode=="random":
        attempt=1
        while True:
            print("attempt: ",attempt)
            seed=randomseed(size,25,27)
            if checksud(seed)==1:
                return seed
            attempt+=1
    elif mode=="rain":

        if lines==[]:
            seed=backtrack(randomseed(size,size*size*size-15,size*size*size-12))
        else:
            lines=makeline(size)
            seed=backtrack(randomseed(size,size+1,size+3),lines)
            displaycompact(seed)
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

            if checksud(seed,lines)!=1:
                seed=oldseed

            for i in range(size*size):
                for y in range(size*size):
                    if isinstance(seed[i][y],int):
                        knowns+=1
        return [seed,lines]

def makeline(size=3,length=4,amo=3):

    lines=[]
    made=False
    
    for i in range(amo):
        seed=False
        while not seed:
            att=[[random.randint(0,size*size-1),random.randint(0,size*size-1)]]
            seed=True
            for x in range(len(lines)):
                if att in lines[x]:
                    seed=False
        lines.append(att)
        for y in range(random.randint(length-2,length+2)):
            growth=False
            tries=0
            while not growth:
                direct=random.randint(1,4)
                if direct==1:
                    att=copy.copy(lines[i][-1])
                    att[0]+=1
                if direct==2:
                    att=copy.copy(lines[i][-1])
                    att[0]-=1
                if direct==3:
                    att=copy.copy(lines[i][-1])
                    att[1]+=1
                if direct==4:
                    att=copy.copy(lines[i][-1])
                    att[1]-=1
                legal=True
                for x in range(len(lines)):
                    if att in lines[x]:
                        legal=False
                if legal:
                    if att[0] in range(size*size):
                        if att[1] in range(size*size):
                            lines[i].append(att)
                            growth=True
                tries+=1
                if tries>8:
                    growth=True
    print(lines, "bruh")
    return lines




