# My project is going to be Tic-Tac-Toe!
# The goal is to make a working project in the IDE / Terminal and then
# expand upon it to the Anvil UI

# Task: Make a TTT game in Python...

# Algorithm:
# 1) Ask the user for input if they want to play the game
# 2) If they do, initialize the lists that will store the game information.
# otherwise, tell the user bye and end the program
# 3) The core gameplay will be as described...
#    -User wants to make a move, they select where to input their symbol (default to x)
#    -The Computer will select from one of the available options and pick a place to go
#           -Random Selection of the number by the computer based on available locations
#    -This continues until someone loses, a cat is drawn, or the user decides to quit
# 4) The player gets a "You win!" screen when they win and a "You lose!" when they lose

# Reformat this to be a double array
board = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
boardValues = list(['', '', '', '', '', '', '', '', ''])

# 1) Ask the user for input if they want to play the game
#   Needs to loop
welcomeMsg = input("Welcome to the Tic-Tac-Toe game... would you like to play? (y/n)")

# This is how I want the board to look when printed
#   1 | 2 | 3
#   4 | 5 | 6
#   7 | 8 | 9
#
def printgameboard():
    for x in range(0, len(boardValues)):
        if x % 3 == 0:
            print(str(board[x]) + boardValues[x] + " |" + "\n")
        else:
            print(str(board[x]) + boardValues[x] + " |")


while welcomeMsg != "n":
    if welcomeMsg.lower() == "y":
        print("Game Start function called.")
        printgameboard()
        break
    else:
        print("Invalid input - call welcome message again")
        welcomeMsg = input("Welcome to the Tic-Tac-Toe game... would you like to play? (y/n)")
