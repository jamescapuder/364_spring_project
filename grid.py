

class Grid():
    SPAWN = 1
    SOURCE = 2

    
    def __init__(self):
        #initialize empty board
        self.board = []
        for i in range(0,50):
            self.board.append([0]*50)

        #set spawn and source locations
        self.board[0][0] = Grid.SPAWN
        self.board[30][40] = Grid.SOURCE
        #initialize list of tuple-states
        self.states = []
        self.createStates()
        

        
    def createStates(self):
        for x in range(Grid.WIDTH):
            for y in range(Grid.HEIGHT):
                if (x, y) not in Grid.OBSTACLES:
                    self.states.append((x, y))
        self.states.append(Grid.ABSORBING_STATE)

        
        
        

if __name__=="__main__":
    g = Grid()
    print(g.board)
