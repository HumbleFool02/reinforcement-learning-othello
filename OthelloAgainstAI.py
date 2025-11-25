from OthelloCanvas import *
from tkinter import *
from OthelloBoard import OthelloBoard
from OthelloController import *
import AlphaBeta
import time
from copy import deepcopy
import time

def reverse(board):
    d = {1: -1, 0:0, -1:1}

    newboard = [[0 for i in range(8)] for j in range(8)]
     
    for i in range(8):
        for j in range(8):
            newboard[i][j] = d[newboard[i][j]]

    return newboard
    
class OthelloSession(object):
    def __init__(self, path):
        self.path = path
        self.root = Tk()
        self.env = OthelloBoard(8)
        self.env.reset()
        
        self.mc = BasicOthelloCanvas(self.root, 8, 8, cellsize = 100)
        self.mc.setBoard(self.env.board)
        
        self.controller = OthelloController(path, 1, epsilon = 10000)
    
    def play(self, load_num):
        self.controller.load([load_num])
        self.controller.population[0].depth = 3
        
        def makeMove(event):
            x, y = self.mc.cell_coords(event.x, event.y)
        
            if(self.env.ValidMove(x,y,1)):
                observation, reward, done, info = self.env.step([x,y])
        
                if(done):
                    black_count = 0
                    white_count = 0
                    for i in range(8):
                        for j in range(8):
                            if self.env.board[i][j] == 1:
                                black_count += 1
                            elif self.env.board[i][j] == -1:
                                white_count += 1

                    print("\n" + "="*40)
                    print("GAME OVER!")
                    print(
                        f"Final Score - Black (You): {black_count} | White (AI): {white_count}")
                    if black_count > white_count:
                        print(
                            f"YOU WIN by {black_count - white_count} pieces!")
                    elif white_count > black_count:
                        print(
                            f"AI WINS by {white_count - black_count} pieces!")
                    else:
                        print("It's a DRAW!")
                    print("="*40 + "\n")
                else:
                    self.mc.setBoard(observation)
                    self.mc.update() 
                    
                    move = self.controller.population[0].policy(observation, -1)
                    
                    observation, reward, done, info = self.env.step(move)
        
                    self.mc.setBoard(self.env.board)
                    self.mc.after(5000, self.mc.update)
            else:
               print("That Move cannot be made, make another one.")
        
        def passMove(event):
            observation, reward, done, info = self.env.step([-1,-1])
        
            if(done):
                print("Done!!!")
            else:
                move = self.controller.population[0].policy(observation, -1)
        
                observation, reward, done, info = self.env.step(move)
        
                self.mc.setBoard(observation)
        
        self.mc.bind("<Button-1>", makeMove)
        self.mc.bind("<Button-2>", passMove)
        self.mc.update()
        
        self.root.mainloop()

    def print_score(self):
        black_count = 0
        white_count = 0
        for i in range(8):
            for j in range(8):
                if self.env.board[i][j] == 1:
                    black_count += 1
                elif self.env.board[i][j] == -1:
                    white_count += 1
        print(f"Black: {black_count} | White: {white_count}")
