import time
import pygame
import os

pygame.font.init()
pygame.display.set_caption("Clicking speed benchmark!")
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.jpg'))
STARTBUTTON = pygame.image.load(os.path.join('Assets', 'startButton.png'))
FONT = pygame.font.SysFont('Adolfine', 100)
FONT2 = pygame.font.SysFont('Adolfine', 150)
WHITE=(255, 255, 255)

def checkClick():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
    else:
        return False


def chceckStart():
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x > 835 and x < 835+351 and y > 390 and y < 390+240:
                return True
            else:
                return False

def showEndScreen(clicks,cps):
    clicks=str(clicks)
    time=" clicks in five seconds cps: "
    cps=str(cps)
    data=clicks+time+cps 
    text=FONT2.render(data,1,WHITE)
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(text, (WIDTH/2-text.get_width() /
             2, HEIGHT/2-text.get_height()/2))
    pygame.display.update()


def showTimeAndClicks(time,clicks):
    time=str(time)
    clicks=str(clicks)
    text2=FONT.render(clicks ,1,WHITE)
    text=FONT.render(time ,1,WHITE)
    WIN.blit(text, (200,400))
    WIN.blit(text2, (200,600))
    pygame.display.update()

def render():
    WIN.blit(BACKGROUND, (0, 0))
    pygame.display.update()


def renderStart():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(STARTBUTTON, (835, 390))
    pygame.display.update()

renderStart()
def main():
    clock = pygame.time.Clock()
    clicks = 0
    start = chceckStart()

    if start:

        timeout = time.time() + 5

        while time.time() < timeout:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0

            render()

            if(checkClick()):
                clicks += 1
            remeaningTime=(time.time()-timeout)*-1
            showTimeAndClicks(int(remeaningTime),clicks)
    else:
        time.sleep(0.2)
        main()

    if clicks>0:
        showEndScreen(clicks,clicks/5)
        time.sleep(7)
        
main()


