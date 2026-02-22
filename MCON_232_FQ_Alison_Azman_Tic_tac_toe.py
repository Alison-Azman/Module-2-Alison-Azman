import random

def print_board(grid):
    for row in range(3):
        for col in range(3):
            print(grid[row][col], end=" ")

        print()

def create_board():
    grid = []
    for r in range(3):              
        rows = []
        for c in range(3):          
            rows.append(" ")
        grid.append(rows)
    return grid

def move(grid, row, col, turn):
    grid[row][col]=turn

def user_turn(grid):
    user_pick= input("Enter a selection row,column ").strip()

    while "," not in user_pick:
        print("That is not a valid selection, needs to be an order pair")
        user_pick = input("Enter a selection row,column ").strip()

    user_pick=user_pick.split(",")

    while len(user_pick) !=2:
        print("That is not a valid selection, needs to be only 2 numbers")
        user_pick = input("Enter a selection row,column ").strip()
        user_pick=user_pick.split(",")

    user_row= int(user_pick[0])
    user_col= int(user_pick[1])

    while user_row >2 or user_row<0:
        print("That is not a valid selection, the row is out of range")
        user_pick = input("Enter a selection row,column ").strip().split(",")
        user_row= int(user_pick[0])
        user_col= int(user_pick[1])

    while user_col >2 or user_col<0:
        print("That is not a valid selection, the column is out of range")
        user_pick = input("Enter a selection row,column ").strip().split(",")
        user_row= int(user_pick[0])
        user_col= int(user_pick[1])

    while grid[user_row][user_col] != " ":
        print("That spot is already picked")
        user_pick = input("Enter a selection row,column ").strip().split(",")
        user_row= int(user_pick[0])
        user_col= int(user_pick[1])

    
    return user_row,user_col


def comp_turn(grid):
    if grid[2][0]=="X" and grid[1][0]=="X" and grid[0][0]==" ":
        return 0,0
    if grid[2][0]=="X" and grid[0][0]=="X" and grid[1][0]==" ":
        return 1,0
    if grid[2][1]=="X" and grid[1][1]=="X" and grid[0][1]==" ":
        return 0,1
    if grid[2][1]=="X" and grid[0][1]=="X" and grid[1][1]==" ":
        return 1,1
    if grid[2][2]=="X" and grid[1][2]=="X" and grid[0][2]==" ":
        return 0,2
    if grid[2][2]=="X" and grid[2][1]=="X" and grid[1][1]==" ":
        return 1,1
    if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]==" ":
        return 0,2
    if grid[0][0]=="X" and grid[0][1]=="X" and grid[1][1]==" ":
        return 1,1
    if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]==" ":
        return 1,2
    if grid[1][0]=="X" and grid[0][1]=="X" and grid[1][1]==" ":
        return 1,1
            
    if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]==" ":
        return 2,2
    if grid[2][0]=="X" and grid[0][1]=="X" and grid[1][1]==" ":
        return 1,1
        
    if grid[0][0]=="X" and grid[2][2]=="X" and grid[1][1]==" ":
        return 1,1
    if grid[0][0]=="X" and grid[0][1]=="X" and grid[1][1]==" ":
        return 1,1
    if grid[0][2]=="X" and grid[2][0]=="X" and grid[1][1]==" ":
        return 1,1
    if grid[0][2]=="X" and grid[0][1]=="X"and grid[1][1]==" ":
        return 1,1
    
    comp_row= random.randint(0,2)
    comp_col= random.randint(0,2)
    while grid[comp_row][comp_col] != " ":
        comp_row= random.randint(0,2)
        comp_col= random.randint(0,2)
    
    return comp_row, comp_col



def winner(grid):
    winner=""
    for r in range(3):
        if grid[r][0]==grid[r][1] and grid[r][0]== grid[r][2]:
            if grid[r][0]!= " ":
                winner=grid[r][0]
    for c in range(3):
        if grid[0][c]==grid[1][c] and grid[0][c]== grid[2][c]:
            if grid[0][c]!= " ":
                winner=grid[0][c]

    if grid[2][0]==grid[1][1] and grid[2][0]== grid[0][2]:
        if grid[2][0]!=" ":
            winner= grid[2][0]

    if grid[0][0]==grid[1][1] and grid[0][0]== grid[2][2]:
        if grid[0][0]!=" ":
            winner= grid[0][0]
    return winner



def tie(grid):
    total=0
    for r in range(3):
        for c in range(3):
            if grid[r][c]!=" ":
                total+=1
    if total==9:
        return True
    else:
        return False



user="X"
comp="O"
user_wins=0
comp_wins=0
ties=0
win=""

play= input("Do you want to play tic tac toe? y/n: ").lower()
print("You are X and the computer is O ")
while play=="y":
    turns=True
    print("The grid looks like this:")
    print(" 0 1 2\n0\n1\n2")
    grid=create_board()
    print_board(grid)
    while turns: #keeps running until there is a winner or a tie
        #User's turn
        user_row, user_col = user_turn(grid)
        move(grid, user_row, user_col,user)
        print("Your move, You are X")
        print("This is the board")
        print_board(grid)
        print()
        win= winner(grid)
        if win != "":
            print(f"The winner is {win}!")
            if win== "X":
                user_wins+=1
                turns=False
            else:
                comp_wins+=1
                turns=False
            break
            
        if tie(grid):
            print("It's a tie")
            ties+=1
            turns=False
            break

        print()
        print()
        #Computer turn
        print("Computer's turn, Computer is O")
        print("This is the board")
        comp_row,comp_col=comp_turn(grid)
        move(grid,comp_row,comp_col, comp)
        print_board(grid)
        print()
        win=winner(grid)
        if win != "":
            print(f"The winner is {win}!")
            if win== "X":
                user_wins+=1
                turns=False
            else:
                comp_wins+=1
                turns=False
            break
        
            
        if tie(grid):
            print("It's a tie")
            ties+=1
            turns=False
            break

        
    print("**************************************************")
    print(f"Scoreboard:\nUser Wins: {user_wins}\nComputer Wins: {comp_wins}\nTie Games: {ties}")       
    play= input("Do you want to play tic tac toe? y/n: ").lower()
print("Thanks for playing!")

