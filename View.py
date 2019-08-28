from abc import ABC, abstractmethod
import Model

class View(ABC): 
    board = [[]]

    def __init__(self, model):
        self.board = model.getBoard()

    @abstractmethod
    def display(self):
        pass

class ConsoleView(View):
    def display(self):
        print("   |   |   ")
        print(" " + self.board[0][0] + " | " + self.board[1][0] + " | " + self.board[2][0] + " ") 
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + self.board[0][1] + " | " + self.board[1][1] + " | " + self.board[2][1] + " ") 
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" " + self.board[0][2] + " | " + self.board[1][2] + " | " + self.board[2][2] + " ") 
        print("   |   |   ")

class TwitterView(View):
    def display(self):
        pass

class MiniView(View):
    def display(self):
        print("┌---┐")
        print("|" + self.board[0][0] + self.board[1][0] + self.board[2][0] + "|") 
        print("|" + self.board[0][1] + self.board[1][1] + self.board[2][1] + "|")
        print("|" + self.board[0][2] + self.board[1][2] + self.board[2][2] + "|")
        print("└---┘")