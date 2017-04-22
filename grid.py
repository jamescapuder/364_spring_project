

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

        
        
        
        

if __name__=="__main__":
    g = Grid()
    print(g.board)
