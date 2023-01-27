class Couloir:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'gray'
    
class Mur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Perso:
    def __init__(self, name, x, y, gold = 0, armor = 5, hits = 12, ):
        self.name = name
        self.x = x
        self.y = y
        self.gold = gold
        self.armor = armor
        self.hits = hits

        
