import grid

def validNextTest():
    g = grid.Grid()
    print("action up from 0,0 is not valid:\n")
    print(g.isValidAction((0,0), "up") == False)
    print("action down from 0,0 is valid:\n")
    print(g.isValidAction((0,0), "down")==True)
    print("action up from 30, 41 is not valid")
    print(g.isValidAction((30,41), "up") == False)


def main():
    validNextTest()
main()
