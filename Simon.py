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