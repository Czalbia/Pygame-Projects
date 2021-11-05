import pygame
import os
import time

pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 240

# GAME SPRITES
pygame.display.set_caption("Tic Tac Toe - epic duel")
BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.png'))
CIRCLE = pygame.image.load(os.path.join('Assets', 'circle.png'))
TRIANGLE = pygame.image.load(os.path.join('Assets', 'triangle.png'))

# WINDOW SETTINGS
WIDTH, HEIGHT = 720, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont('comicsans', 250)
FONT2 = pygame.font.SysFont('comicsans', 100)

def showText(text):
    draw_text = FONT2.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2-draw_text.get_width() /
             2, HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)


def showWinner(text):
    draw_text = FONT.render(text+" wins!", 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2-draw_text.get_width() /
             2, HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)
    quit()

def showTie():
    draw_text = FONT.render("   Tie!", 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2-draw_text.get_width() /
             2, HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)
    quit()

def render(board):
    POS={
        0 : (20,20),
        1 : (260,20),
        2 : (500,20),
        3 : (20,260),
        4 : (260,260),
        5 : (500,260),
        6 : (20,500),
        7 : (260,500),
        8 : (500,500) }
    WIN.blit(BACKGROUND, (0, 0))
    for i in range(len(board)):
        if(board[i]=='X'):
            WIN.blit(TRIANGLE, POS[i])
        elif(board[i]=='O'):
            WIN.blit(CIRCLE, POS[i])
            
    pygame.display.update()


clock = pygame.time.Clock()
def main(board):
    timeout = time.time() + 0.1
    while time.time()<timeout:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
        render(board)
