
class State():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x,y)
        self.carry = 0 
        self.capacity = 1

    def updateCoords(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x,y)
