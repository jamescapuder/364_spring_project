class Source():
    def __init__(self, x, y, capacity=100000):
        self.x = x
        self.y = y
        self.coords = (x, y)

    def gather(self):
        if capacity == 0:
            return False
        else:
            self.capacity -= 1
            return True
