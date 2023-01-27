from Simon import *
from clemclem import *

#trucs utiles
RED = (174, 74, 52)
GRAY = (204, 204, 204)
BROWN = (248, 142, 85)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (249, 66, 158)
PURPLE = (128, 0, 128)


GAUCHE = (-1, 0)
DROITE = (1, 0)
HAUT = (0, -1)
BAS = (0, 1)

def somme(x : tuple, y: tuple):
    a, b = x
    c, d = y
    return a+c, b+d

#classes
class Couloir:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = GRAY
    
class Mur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BROWN

class Perso:

    def __init__(self, x, y, name = 'Luc', gold = 0, armor = 5, hits = 12):
        self.name = name
        self.x = x
        self.y = y
        self.gold = gold
        self.armor = armor
        self.hits = hits
        self.color = RED
    
    def change_position(self, direction):
        self.x, self.y = somme((self.x, self.y), direction)

        
