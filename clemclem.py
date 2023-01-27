class Sol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'white'
        self.move = False
        self.through = True

class Vide:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'black'
        self.move = False 
        self.through = False


class Potion:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.move = False


