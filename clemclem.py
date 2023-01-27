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



etage, heros, collectables = convert_text2lab('premier_etage.txt')
position_gold, position_potion = generation_objet(etage)
#invent = Inventaire()
collectables_simon = {position_gold : Gold(position_gold[0], position_gold[1]), position_potion : Potion(position_potion[0], position_potion[1])}

pg.init()
screen = pg.display.set_mode((LONGUEUR, LARGEUR))
clock = pg.time.Clock()

running = True

while running:

    clock.tick(10)

    rect = pg.Rect(0, 0, LONGUEUR, LARGEUR)
    pg.draw.rect(screen, WHITE, rect)

    for ligne in etage:
        for objet in ligne:
            if not objet.move:
                rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
                pg.draw.rect(screen, objet.color, rect)
    
    for position, objet in collectables.items():
        rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
        pg.draw.rect(screen, objet.color, rect)

    for position, objet in collectables_simon.items():
        rect = pg.Rect(FD*objet.x, FD*objet.y, FD, FD)
        pg.draw.rect(screen, objet.color, rect)

   # if (heros.x, heros.y) == position_potion : 
        invent.get_potion()
        del collectables_simon[position_potion]



