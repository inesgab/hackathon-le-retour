class Sol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'white'
        self.move = False
        self.through = True
        self.gettable = False

class Vide:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'black'
        self.move = False 
        self.through = False
        self.gettable = False


class Potion:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.move = False
        self.gettable = True        
        self.color = 'blue'


class Inventaire:
    def __init__(self):
        self.items = {'potion' : 0, 'armure' : 0}

    def get_potion(self):
        if self.items['potion'] < 5 :
            self.items['potion'] += 1

    def get_armure(self):
        if self.items['armure'] < 5 :
            self.items['armure'] += 1        





