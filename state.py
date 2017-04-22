
class State():
    def __init__(x,y):
        self.x = x
        self.y = y
        self.coords = (x,y)
        self.is_carrying = False

    def updateCoords(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x,y)
