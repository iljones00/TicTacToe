import Model
from View import View, ConsoleView, MiniView
from Strategies import *


def main():
    model = Model.Model(3, 3)
    view = MiniView(model)
    strategy = playAnyOpenPosition(model)
    print("This is the game of Tic Tac Toe")
    print("Moves must be made in the format 'x,y' where x and y are the coordinates of your move")
    gameIsPlaying = True
    while True:
        players = model.setStart()
        turn = model.chooseStart()
        currentTurn = -1
        if turn: 
            print("You will start")
            currentTurn = 0
        else:
            print("I will start")
            currentTurn = 1
        while gameIsPlaying:
            if turn:
                model.receiveInput(players[0])
                view.display()
                if model.isWinner(players[0]):
                    print("You won.")
                    gameIsPlaying = False
            else:
               print("Thinking...")
               time.sleep(2)
               strategy.makeMove(players[1])
               view.display()
               if model.isWinner(players[1]):
                    print("I won!!!")
                    gameIsPlaying = False
            turn = not turn
            if model.isGameOver():
                print("No one wins")
                break
            
        if not model.playAgain():
            print("Thanks for playing!")
            break

main()
