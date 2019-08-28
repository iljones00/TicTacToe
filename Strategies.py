from abc import ABC, abstractmethod
import Model
import time

class Strategy(ABC):

    def __init__(self, model):
        self.model = model

    @abstractmethod
    def makeMove(self, player):
        pass

class playAnyOpenPosition(Strategy, object):
    def makeMove(self, player):
        for j in range(len(self.model.getBoard()[0])):
            for i in range(len(self.model.getBoard())):
                if self.model.getBoard()[i][j] == " ":
                    self.model.makeMove(i, j, player)
                    return