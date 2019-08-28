import random

class Model(object):
    rows = 3
    columns = 3
    board = [[]]

    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.board = [[" " for i in range(self.columns)] for j in range(self.rows)] 

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [[" " for i in range(self.columns)] for j in range(self.rows)] 

    def display(self) :
        print("   |   |   ")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " ") 
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " ") 
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " ") 
        print("   |   |   ")

    def makeMove(self, x, y, player):
        if x < 0 or y < 0 or x >= self.rows or y >= self.columns:
            raise ValueError("x or y input is off the board")
        if self.board[x][y] != " ":
            raise Exception("A piece is already in this position, please try again")
        self.board[x][y] = player

    def isWinner(self, player):
        return ((self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player) or 
        (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player) or 
        (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player) or 
        (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player) or 
        (self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player) or 
        (self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player) or 
        (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or 
        (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player))

    def isGameOver(self):
        for j in range(self.columns):
            for i in range(self.rows):
                if self.board[i][j] == " ":
                    return False
        return True
    
    def getBoard(self):
        return self.board
    
    def receiveInput(self, player):
        incoming = input()
        if (len(incoming) != 3 or incoming[1] != ',' or not incoming[0].isdigit() or not incoming[2].isdigit()):
            print("Input is of incorrect style. All inputs should follow the format 'x,y'")
            self.receiveInput(player)
            return
        elif int(incoming[0]) > self.columns - 1 or int(incoming[0]) < 0 or int(incoming[2]) > self.rows - 1 or int(incoming[2]) < 0:
            print("Values must be on the board. Try again")
            self.receiveInput(player)
            return
        elif self.board[int(incoming[0])][int(incoming[2])] != " ":
            print("Piece is already in that position. Try again")
            self.receiveInput(player)
            return
        self.makeMove(int(incoming[0]), int(incoming[2]), player) 
    
    def resetBoard(self):
        for j in range(self.columns):
            for i in range(self.rows):
                self.board[i][j] = " "

    def playAgain(self):
        print('Play again? (yes or no)')
        inputString = input().lower()
        if inputString != "yes" and inputString != "no":
            print("Sorry, I didn't quite catch that")
            self.playAgain()
            return
        else :
            return inputString == "yes"

    def setStart(self):
        print("Select a piece: X or O")
        inputString = input().lower()
        if inputString != 'x' and inputString != 'o':
            print("Sorry, I don't understand what you said. Please try again")
            self.setStart()
        if inputString == "x":
            return ['X', 'O']
        else:
            return ['O', 'X']

    def chooseStart(self):
        return random.randint(0, 1) == 0
    
    def switchTurns(self):
        self.turn = not self.turn
    