import numpy
def printboard(Board):                  # quick little Function which prints the current board
    for row in Board:
        for elem in row:
            print(elem, end=' ')
        print()


def possible(y, x, n, Board):           # Function checks wether a number n can be placed at the spot[y/x]
    for i in range(len(Board)):         # checks Rows
        if Board[y][i] == n:
            return False
    for i in range(len(Board)):         # checks Columns
        if Board[i][x] == n:
            return False
    x0 = (x // 3) * 3                   # checks Squares
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if Board[y0 + i][x0 + j] == n:
                return False
    return True


def solver(Board):                                      # backtracking Algorithm
    for y in range(9):
        for x in range(9):
            if Board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n, Board):
                        Board[y][x] = n
                        solver(Board)                   #recursion
                        Board[y][x] = 0
                return
    print(numpy.matrix(Board))
    input("Next Possible Solution?: " )

solver([[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]])
