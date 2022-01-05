
gameStillGoing = True
winner = None
currentPlayer = "x"
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def playGame():
    # display the board
    displayBoard()

    while (gameStillGoing):
        handleTurn(currentPlayer)
        checkGameOver()
        flipPlayer()

    #game ended 
    if(winner == "x" or winner == "o"):
        print(winner + " is the winner ;)")
    elif(winner == None):
        print("It's a tie :/")
 


def handleTurn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1 to 9: ")
    
    valid = False
    while not valid : 
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Please choose another place.")

    board[position] = player
    displayBoard()

def checkGameOver():
    checkWin()
    checkTie()

def checkWin():

    global winner 

    #check rows
    rowWin = checkRows()
    #check columns
    colWin = checkColoumns()
    #check diagonals 
    diagWin = checkDiagonals()

    if rowWin:
        #win
        winner = rowWin
    elif colWin:
        #win
        winner = colWin
    elif diagWin:
        #win
        winner = diagWin
    else:
        #no win
        winner = None
    return

def checkRows():
    global gameStillGoing

    firstRow = board[0] == board[1] == board[2] != "-"
    secondRow = board[3] == board[4] == board[5] != "-"
    thirdRow = board[6] == board[7] == board[8] != "-"
    
    if firstRow or secondRow or thirdRow:
        gameStillGoing = False

    #return winner - x or o
    if firstRow:
        return board[0]
    if secondRow:
        return board[3]
    if thirdRow:
        return board[7]

    return

def checkColoumns():
    global gameStillGoing

    firstCol = board[0] == board[3] == board[6] != "-"
    secondCol = board[1] == board[4] == board[7] != "-"
    thirdCol = board[2] == board[5] == board[8] != "-"
    
    if firstCol or secondCol or thirdCol:
        gameStillGoing = False

    #return winner - x or o
    if firstCol:
        return board[0]
    if secondCol:
        return board[1]
    if thirdCol:
        return board[2]

    return 

def checkDiagonals():
    global gameStillGoing

    firstDiag = board[0] == board[4] == board[8] != "-"
    secondDiag = board[2] == board[4] == board[6] != "-"
    
    if firstDiag or secondDiag:
        gameStillGoing = False

    #return winner - x or o
    if firstDiag:
        return board[0]
    if secondDiag:
        return board[2]

    return 


def checkTie():
    global gameStillGoing

    if("-" not in board):
        gameStillGoing = False
    return 


def flipPlayer():
    global currentPlayer

    if (currentPlayer == "x"):
        currentPlayer = "o"
    elif (currentPlayer == "o"):
        currentPlayer = "x"

    return




playGame()


#play game
#handle turns
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip between players
