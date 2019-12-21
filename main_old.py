<<<<<<< Updated upstream
import numpy as np
=======
<<<<<<<< Updated upstream:main_old.py
import numpy as np


>>>>>>> Stashed changes
class Card:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

<<<<<<< Updated upstream
class Servant(Card):
    kind = "Servant"
    def __init__(self, name, cost):
        super().__init__(name, cost)


=======

class Servant(Card):
    kind = "Servant"

    def __init__(self, name, cost):
        super().__init__(name, cost)

>>>>>>> Stashed changes
    def display(self):
        print("%s is a %s card (cost: %d)" % (self.name, Servant.kind, self.cost))


<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
class Soldier:
    def __init__(self, name, HP, ATK, DEF):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

    def attack(self, enemy) -> None:
        Rules.attack(self, enemy)
        print("%s attack %s" % (self.name, enemy.name))
        print(f"{enemy.name}'s HP: {enemy.HP}")
<<<<<<< Updated upstream
    
    def display(self):
        print(f"[{self.name}] HP: {self.HP} ATK: {self.ATK} DEF: {self.DEF}")
        
=======

    def display(self):
        print(f"[{self.name}] HP: {self.HP} ATK: {self.ATK} DEF: {self.DEF}")


>>>>>>> Stashed changes
class Player:
    def __init__(self, name="BILLY", HP=30, GOLD=1):
        self.GOLD = GOLD
        self.HP = HP
        self.name = name

    def display(self):
        print("%s's GOLD: %s" % (self.name, self.GOLD))

<<<<<<< Updated upstream
class BattleField:
    def __init__(self, max_num):
        self.max_num = max_num
        self.battle = [[],[]]
=======

class BattleField:
    def __init__(self, max_num):
        self.max_num = max_num
        self.battle = [[], []]
>>>>>>> Stashed changes
        self.actionQueue = []

    def add(self, what: Soldier, owner: int):
        if len(self.battle[owner]) > self.max_num:
            print("Already full!")
        else:
            self.battle[owner].append(what)

    def remove(self, what: Soldier, owner: int):
        self.battle[owner].remove(what)
<<<<<<< Updated upstream
    
=======

>>>>>>> Stashed changes
    def beginBattle(self):
        pass
        # for player_index in range(2):
        #     for _soldier in self.battle[player_index]:
        #         _soldier.cd = 100
        # while(True):
        #     for player_index in range(2):
        #         for _soldier in self.battle[player_index]:
        #             Rules.update_cd(_soldier)
        #             if _soldier.cd < 0:
        #                 _soldier.attack()

    def display(self):
        print("Player 1 has soldiers:")
        for i in range(len(self.battle[0])):
            self.battle[0][i].display()
        print("Player 2 has soldiers:")
        for i in range(len(self.battle[1])):
            self.battle[1][i].display()

<<<<<<< Updated upstream
class Phase:
    MAX_SOLDIER_NUM = 10
=======

class Phase:
    MAX_SOLDIER_NUM = 10

>>>>>>> Stashed changes
    def __init__(self):
        self.battleField = BattleField(Phase.MAX_SOLDIER_NUM)

    def battlePhase(self):
        pass


<<<<<<< Updated upstream

class Rules():
    @staticmethod
    def attack(attacker: Soldier, defender: Soldier) :
=======
class Rules:
    @staticmethod
    def attack(attacker: Soldier, defender: Soldier):
>>>>>>> Stashed changes
        defender.HP -= attacker.ATK - defender.DEF

    @staticmethod
    def update_cd(foo: Soldier):
        foo.speed = 1
        foo.cd -= foo.speed

<<<<<<< Updated upstream
# test
if __name__ == "__main__":
    
=======

# test
if __name__ == "__main__":
>>>>>>> Stashed changes
    a = Player()
    a.display()
    b = Servant("Gobllin", 1)
    b.display()

    s1 = Soldier("soldier uu", 10, 5, 1)
    s3 = Soldier("soldier kk", 10, 5, 1)
    s2 = Soldier("soldier jj", 10, 2, 1)
    s1.attack(s2)
    print("------------")
    p = Phase()
    p.battleField.add(s1, 0)
    p.battleField.add(s3, 0)
    p.battleField.add(s2, 1)
<<<<<<< Updated upstream
    p.battleField.display()
=======
    p.battleField.display()
========
import pygame, sys
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
basicFont = pygame.font.SysFont(None, 48)

def m_drawText(x, y, s, font):
    # set up the text
    text = font.render(s, True, BLACK)
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y    
    # draw the text onto the surface
    windowSurface.blit(text, textRect)

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



pos = ""
# run the game loop
while True:
    pygame.time.wait(10)
    windowSurface.fill(WHITE)
    m_drawText(100, 100, str(pos), basicFont)
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            

    # draw the window onto the screen
    pygame.display.update()
>>>>>>>> Stashed changes:main.py
>>>>>>> Stashed changes
