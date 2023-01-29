"""


"""

playerOne = None
board = None


# Print Board
def printBoard():
    print(f"   |   |   \n {board[1]} | {board[2]} | {board[3]} \n   |   |   \n-----------\n   |   |   \n {board[4]} | {board[5]} | {board[6]} \n   |   |   \n-----------\n   |   |   \n {board[7]} | {board[8]} | {board[9]} \n   |   |   \n")


def makeMove(position, symbol):
    board[position] = symbol
    print(f"\n\n{symbol} made move at {position}")


def playerTurn():
    x = 0
    while True:
        try:
            x = input("Enter your move position: ")
            x = int(x)
            if x not in range(1, 10):
                print("Enter number between 1-9")
                continue

            if board[x] != " ":
                print("This position is already marked.")
                print("You can choose " + str(avaliablePositions()) +
                      " one of these numbers.")
                continue

        except:
            print("Enter valid Number")
            continue
        break
    return x


#Computer Turn
def computerTurn():
    avaliableMoves = avaliablePositions()

    #Check if O have a winning move
    #Brute Force
    for i in avaliableMoves:
        tempBoard = board[:]
        tempBoard[i]="O"
        if checkWinner(tempBoard):
            print("winnerMove")
            return i

    #Check if X is winning then block that win move
    #Brute Force
    for k in avaliableMoves:
        tempBoard = board[:]
        tempBoard[k]="X"
        if checkWinner(tempBoard):
            print("BlockMove")
            return k

    import random
    return random.choice(avaliableMoves) 


# Computer Turn()
def playerOneTurn():
    
    if playerOne:
        return playerTurn()
    else:
       return computerTurn()
    


# Return List of avaliable positions
def avaliablePositions():
    tempArray = []
    for i in range(1, 10):
        if board[i] == " ":
            tempArray.append(i)
    return tempArray


# Check for winner
# Return Boolean, True= Winner, False=No Winner
def checkWinner(checkBoard):
    possibleWinner = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in possibleWinner:

        if checkBoard[x[0]] == checkBoard[x[1]] == checkBoard[x[2]] and checkBoard[x[0]] != " ":
            return True

    return False


# Choose between Human vs Human or Computer vs Human
def selectPlayer():
    global playerOne
    print("Choose:\n1. Two Player(Human vs Human)\n2. One Player(Human vs Computer)")
    x = input("Select '1' or '2': ")
    if x == "1":
        playerOne = True
    else:
        playerOne = False


def main():
    global board
    board = [0, " ", " ", " ", " ", " ", " ", " ", " ", " "]

    selectPlayer()
    printBoard()
    while True:

        makeMove(playerOneTurn(), "O")
        printBoard()
        if checkWinner(board):
            print("\nO Won the game")
            break
        if len(avaliablePositions()) == 0:
            print("Game is Tie")
            break

        makeMove(playerTurn(), "X")
        printBoard()
        if checkWinner(board):
            print("\nX Won the game")
            break
        if len(avaliablePositions()) == 0:
            print("Game is Tie")
            break
    print("Nice game")


def clearConsole():
    import os

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
    cls()


# Start Code
print("Welcome to Tic-Tac-Toe")
while True:
    main()

    # Play again
    print("Play again?")
    again = input("Y/N: ")

    if again == "y" or again == "Y":
        clearConsole()
        continue
    else:
        print("\n\n---------------------\n Thank You :)\nCome Back Soon\n CodedBy:0001\n---------------------")
        break



"""
Thanks


"""
