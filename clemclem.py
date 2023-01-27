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


