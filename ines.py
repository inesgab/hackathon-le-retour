from Simon import *
from clemclem import *

class Couloir:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'gray'
    
class Mur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'brown'

class Perso:

    def __init__(self, x, y, name = 'Luc', gold = 0, armor = 5, hits = 12):
        self.name = name
        self.x = x
        self.y = y
        self.gold = gold
        self.armor = armor
        self.hits = hits
        self.color = 'red'

classes = {
    "#" : Couloir,
    "|" : Mur,
    "-" : Mur,
    "@" : Perso,
    "+" : Porte,
    " " : Vide,
    "." : Sol,
    "=" : Escalier
}

        
