import random

print("Welcome to Tic Tac Toe!")
print("--------------------------------")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
    for i in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(cols):
            [print("", gameBoard[i][j], end=" |")]
    print("\n+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    row = num // 3
    col = num % 3
    gameBoard[row][col] = turn

def checkWinner():
    # Check rows and columns
    for i in range(rows):
        if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2]:
            return gameBoard[i][0]
        if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i]:
            return gameBoard[0][i]
    
    # Check diagonals
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]
    
    return None 

leaveLoop = False    
counter = 1

while(leaveLoop == False):
    printGameBoard()
    winner = checkWinner()
    if winner:
        print(f"\n{winner} wins!")
        break
    if len(possibleNumbers) == 0:
        print("\nIt's a draw!")
        break
    ## user's turn
    if(counter % 2 == 1):
        # printGameBoard()
        pickedNum = int(input("\nPick a number [1-9]: "))
        if(pickedNum >= 1 and pickedNum <= 9):
            if(pickedNum in possibleNumbers):
                 modifyArray(pickedNum, 'X')
                 possibleNumbers.remove(pickedNum)
                 counter += 1
            else:
                print("number choosen , try different one:")
        else: 
            print("Invalid input, Try again")
    ## machine's turn
    else:
         while(True):
             machineChoice = random.choice(possibleNumbers)
             print("Machine choice is ", machineChoice)
             if(machineChoice in possibleNumbers):
                 modifyArray(machineChoice, 'O')
                 possibleNumbers.remove(machineChoice)
                 counter += 1
                 break





# printGameBoard()