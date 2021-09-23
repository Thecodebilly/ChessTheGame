import chess
import pygame
import random
board = chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
print(board)

#colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (164, 74, 74)
GREEN = (0, 255, 0)
GRASS = (30, 200, 0)
ORANGE = (255, 69, 0)
GRAY = (128, 128, 128)
BROWN = (205, 133, 63)

#dimensions
xscaled = 0
yscaled = 0
width = 50
height = 50
scale = 10
unit = scale - 1
arenasize = scale * width + 1

#start screen
pygame.init()
screen = pygame.display.set_mode((arenasize, arenasize))
pygame.display.set_caption('CHESS')
screen.fill(WHITE)
pygame.display.update()
#start chess loop

def gameOver(board):
    status=0

    #returns 0 if the game is still to be played
    if status==0:
        return status
    #returns another number if the game is over
    else:


while(not gameOver()):
