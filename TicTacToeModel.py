class TicTacToeModel(object):
    rows = 3
    columns = 3
    players = 2
    arr = [[]]
    turn = 0

    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.players = 2
        self.arr = [[" " for i in range(columns)] for j in range(rows)] 

    def __init__(self, rows, columns, players):
        self.rows = rows
        self.columns = columns
        self.players = players
        self.arr = [[" " for i in range(columns)] for j in range(rows)] 

    def display(self) :
        print("   |   |   ")
        print(" " + self.arr[0][0] + " | " + self.arr[0][1] + " | " + self.arr[0][2] + " ") 
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + self.arr[1][0] + " | " + self.arr[1][1] + " | " + self.arr[1][2] + " ") 
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + self.arr[2][0] + " | " + self.arr[2][1] + " | " + self.arr[2][2] + " ") 
        print("   |   |   ")

    def makeMove(self, x, y, player):
        if (x < 0 or y < 0 or x >= self.rows or y >= self.columns):
            raise ValueError("x or y input is off the board")
        if (self.arr[x][y] != " "):
            raise Exception("A piece is already in this position, please try again")
        self.arr[x][y] = player

tttmodel = TicTacToeModel(3, 3, 2)
tttmodel.display()
tttmodel.makeMove(0, 0, 'X')
tttmodel.display()

    