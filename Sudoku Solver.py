Board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def printboard():
    global Board
    for row in Board:
        for elem in row:
            print(elem, end=' ')
        print()

def possible(x, y , n):
    global Board
    for i in range(len(Board)):
        if Board[x][i] == n:
            print("False")
            return False

    for j in range(len(Board)):
        if Board[i][y] == n:
            print("False")
            return False

    y0 = (x//3)*3
    x0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if Board[y0+1][x0+1] == n:
                print("False")
                return False

    return True

printboard()
possible(4,4,3)