
class State():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x,y)
        self.is_carrying = False
        self.capacity = 100000

    def updateCoords(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x,y)
