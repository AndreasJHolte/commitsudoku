import math
import copy
import random
from create2 import *
from solvers import *
from interface import *




def main():


    print("greetings, what would you like to do?")

    while True:

        
        board=[]
        print("main menu")
        print("create new sudoku (1)")
        print("input your own sudoku (2)")
        print("exit (3)")
        choices=3
        mainchoice=0
        while mainchoice not in range(1,choices+1):
            mainchoice=input("choice: ")
            if mainchoice.isdigit():
                mainchoice=int(mainchoice)
      

        lines=[]
        if mainchoice==1:
            
            
            print("what boardsize do you want? (from 1 through 5)")
            print("(4 and 5 are not recommended as they can take a long time, especially 5)")
            choices=5
            choice=0
            while choice not in range(1,choices+1):
                choice=input("choice: ")
                if choice.isdigit():
                    choice=int(choice)
            size=copy.copy(choice)
            print("which difficulty? (1,2, or 3)")
            choices=3
            choice=0
            while choice not in range(1,choices+1):
                choice=input("choice: ")
                if choice.isdigit():
                    choice=int(choice)
            difficulty=copy.copy(choice)


            print("do you want the line variant rule? (1 for no, 2 for yes)")
            print("this rules makes lines where each neighbor must have a difference")
            print("of at least 3")
            choices=2
            choice=0
            while choice not in range(1,choices+1):
                choice=input("choice: ")
                if choice.isdigit():
                    choice=int(choice)
            lines=[]
            if choice==2:
                lines=0
            
            [board,lines]=findunique(size,lines,difficulty)
        

        if mainchoice==2:
            
            print("there are two methods of inputting a sudoku:")
            print("manual (1) or in a list format (2)")
            
            
            choices=2
            choice=0
            while choice not in range(1,choices+1):
                choice=input("choice: ")
                if choice.isdigit():
                    choice=int(choice)
            formatt=copy.copy(choice)
            
            print("what boardsize do you want? (from 1 through 5)")
            choices=5
            choice=0
            while choice not in range(1,choices+1):
                choice=input("choice: ")
                if choice.isdigit():
                    choice=int(choice)
            size=copy.copy(choice)
            
            if formatt==1:
                building=True
                board=createboard(size)
                while building:
                    displaycompact(board)

                    change=numinput(size*size)
                    board[int(change[0])][int(change[1])]=int(change[2])

                    cont=input("do you want to continue? (y/n)")

                    if cont=="n":
                        building=False

            if formatt==2:
                trying=True
                board=createboard(size)
                while trying:
                    
                    print("the format is purely numbers and commas counting from the top left")
                    print("corner rightwards, starting again at the left of the next row")
                    print("for a 9 by 9 this would be 81 numbers and 80 commas")
                    print("in the format 9,2,3,6,4 etc")
                    attempt=input("please enter the sudoku:")

                    listed=attempt.strip(",")
                    x=0
                    trying=False
                    for i in range(size*size):
                        for y in range(size*size):
                            if listed[x].isdigit():
                                board[i][y]=int(listed[x])
                            else:
                                trying=True

                            x+=1

        if mainchoice==3:
            print("bye")
            break

        if len(board)>0:
            puzzling=True
            while puzzling:
                
                print("you have a sudoku, what do you want to do with it")
                print("solve it (1)")
                print("display it (2)")
                print("check how many solutions it has (3)")
                print("solve it myself (4)")
                print("check if it is solved (5)")
                print("discard the sudoku (6)")

                choices=6
                choice=0
                while choice not in range(1,choices+1):
                    choice=input("choice: ")
                    if choice.isdigit():
                        choice=int(choice)
                choice=copy.copy(choice)

                if choice==1:
                    if len(checkamo(board,lines)[1])==1:
                        board=backtrack(board,lines)
                        displaycompact(board)
                    else:
                        print("this is not a well formed sudoku")
                if choice==2:
                    displaycompact(board)
                if choice==3:
                    soluts=len(checkamo(board,[],-1,-1,lines)[1])
                    if soluts>1:
                        print("this board has multiple solutions")
                    if soluts==1:
                        print("this board has exactly one solution")
                    if soluts<1:
                        print("this board has no solutions")
                if choice==4:
                    building=True
                    while building:
                        displaycompact(board)
                        ines=[]
                        
                        for i in range(len(lines)):
                            ines.append([lines[i][0].reverse()])
                            for y in range(len(lines[i])-1):
                                ines[i].append(lines[i][y+1].reverse())
                        if len(ines)>0:
                            print("these are the lines in column,row format: ",lines)

                        change=numinput(size*size)
                        if isinstance(board[int(change[0])][int(change[1])],int):
                            print("you are overwriting a number, this number was: ",board[int(change[0])][int(change[1])])
                        board[int(change[0])][int(change[1])]=int(change[2])
                        

                        cont=input("do you want to continue? (y/n)")

                        if cont=="n":
                            building=False
                if choice==5:
                    
                    print(checksolve(board))
                    if checksolve(board):
                        print("this sudoku is solved")
                    else:
                        print("this sudoku is not solved")

                if choice==6:
                    break
                print("")



main()




