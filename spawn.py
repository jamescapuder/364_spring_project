class Spawn():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coord = (x, y)
        self.resources = 0
    
    def dropoff(self):
        self.resources += 1

    def reset(self):
        self.resources = 0
