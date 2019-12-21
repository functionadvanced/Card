import pygame
import sys
from pygame.locals import *
from pygame.time import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((1280, 768), 0, 32)
pygame.display.set_caption('Hello world!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
basicFont = pygame.font.SysFont("comicsansms", 20)


def m_drawText(x, y, s, font=basicFont):
    # set up the text
    text = font.render(s, True, BLACK)
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y    
    # draw the text onto the surface
    windowSurface.blit(text, textRect)


class Board:

    def __init__(self):
        pass

    def draw(self):
        w = 15
        h = 15
        for i in range(w):
            for j in range(h):
                pygame.draw.rect(windowSurface, BLACK, (400+i*30, 20+j*30, 28, 28), 1)

class Card:

    def __init__(self, x, y, s_name, s_cost):
        self.x = x
        self.y = y
        self.w = 61.8*2
        self.h = 200
        self.name = s_name
        self.cost = s_cost
        self.active = False

    def is_collide(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x+self.w and pos[1] >= self.y and pos[1] <= self.y+self.h:
            return True
        else:
            return False

    def draw(self):
        active_lift = -20
        temp = "cost: "+str(self.cost)
        if not self.active:
            pygame.draw.rect(windowSurface, BLACK, (self.x-1, self.y-1,
                                                    self.w+2, self.h+2))
            pygame.draw.rect(windowSurface, WHITE, (self.x, self.y,
                                                    self.w, self.h))
            m_drawText(self.x+self.w/2, self.y+self.h/4, self.name)
            m_drawText(self.x+self.w/2, self.y+self.h/2, temp)
        else:
            pygame.draw.rect(windowSurface, BLACK, (self.x-1,
                                                    self.y-1+active_lift, self.w+2, self.h+2))
            pygame.draw.rect(windowSurface, WHITE, (self.x, self.y+active_lift,
                                                    self.w, self.h))
            m_drawText(self.x+self.w/2, self.y+active_lift+self.h/4, self.name)
            m_drawText(self.x+self.w/2, self.y+active_lift+self.h/2, temp)

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# # draw the text's background rectangle onto the surface
# pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray



pos = (0, 0)
card_list = []
for i in range(5):
    card_list.append(Card(20+i*50, 500,"pawn", 1))
board = Board()
# run the game loop
while True:
    pygame.time.wait(10)
    windowSurface.fill(WHITE)
    
    board.draw()
    m_drawText(200, 100, str(pos))
    now_active = -1
    for i, x in enumerate(card_list):
        x.active = False
        if x.is_collide(pos):
            now_active = i
    if now_active != -1:
        card_list[now_active].active = True
    for x in card_list:
        if not x.active:
            x.draw()
    if now_active != -1:
        card_list[now_active].draw()
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
            

    # draw the window onto the screen
    pygame.display.update()
