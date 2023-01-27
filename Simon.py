class Porte : 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'PINK'
        self.move = False
        self.through = True
        self.gettable = False 

class Escalier : 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'GREEN'
        self.move = False 
        self.through = True 
        self.gettable = False 

import random as rd
def fonction(etage):
    position_potion = ()
    position_gold = ()
    m, n = len(etage), len(etage[0])
    while position_potion == () :
        a, b= rd.randint(n), rd.randint(m)
        if type(etage[a][b]) is Sol :
            position_potion = (a, b)
    while position_gold == () :
        a, b = rd.randint(n), rd.randint(m)
        if type(etage[a][b]) is Sol :
            position_gold = (a, b)
    return position_gold, position_potion
        


