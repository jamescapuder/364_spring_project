class Source():
    def __init__(self, x, y, capacity=100000):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.capacity = capacity
        self.og_capacity = capacity

    def gather(self):
        if self.capacity == 0:
            return False
        else:
            self.capacity -= 1
            return True

    def reset(self):
        self.capacity = self.og_capacity
