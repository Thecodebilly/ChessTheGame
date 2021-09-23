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

def isGameOver(board):
    status=0
    if board.is_seventyfive_moves():
        status = 1
    elif board.can_claim_draw():
        status = 2
    elif board.is_stalemate():
        status = 3
    elif board.is_checkmate():
        status = 4
    elif board.is_insufficient_material():
        status = 5
    #returns 0 if the game is still to be played, and non zero for different endings
    return status;


while(isGameOver()==0):
    
    print("insert game")
    


board.clear_stack()










#end pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
