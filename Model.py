class Model(object):
    rows = 3
    columns = 3
    players = 2
    board = [[]]
    turn = 0

    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.players = 2
        self.board = [[" " for i in range(columns)] for j in range(rows)] 

    def __init__(self, rows, columns, players):
        self.rows = rows
        self.columns = columns
        self.players = players
        self.board = [[" " for i in range(columns)] for j in range(rows)] 

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
        if self.isWinner('X') or self.isWinner('O'):
            return True
        for j in range(self.columns):
            for i in range(self.rows):
                if self.board[i][j] == " ":
                    return False
        return True
    
    def getBoard(self):
        return self.board

    
tttmodel = Model(3, 3, 2)
tttmodel.makeMove(0, 0, 'X')
tttmodel.makeMove(1, 0, 'X')
tttmodel.makeMove(2, 0, 'X')
tttmodel.display()
print(tttmodel.isGameOver())

    