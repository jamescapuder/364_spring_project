

class Grid():
    def __init__(self):
        self.board = []
        for i in range(0,50):
            self.board.append([0]*50)
        self.board[1][1] = 1
        
        

if __name__=="__main__":
    g = Grid()
    print(g.board)
