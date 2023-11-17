from typing import List

def a(grid: List[List[int]]):
    y = len(grid)
    x = len(grid[0])
    matrix = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            matrix[i][j] = 0

    if grid[0][0] == 1:
        return 0
    else:
        if x == 1 and y == 1 and grid[0][0] == 0:
            return 1

        elif x == 1 and y == 1 and grid[0][0] == 1:
            return 0

        elif y == 1:
            flag = False
            for i in range(x):
                if grid[0][i] == 1:
                    flag = True
            if flag == True:
                return 0
            else:
                return 1

        elif x == 1:
            flag = False
            for i in range(y):
                if grid[i][0] == 1:
                    flag = True
            if flag == True:
                return 0
            else:
                return 1

        else:
            matrix[0][0] = 1
            for i in range(1,y):
                if grid[i][0] == 1 or matrix[i - 1][0] == 0:
                    matrix[i][0] = 0
                elif grid[i][0] == 0 and matrix[i - 1][0] == 1:
                    matrix[i][0] = 1

            for j in range(1,x):
                if grid[0][j] == 1 or matrix[0][j - 1] == 0:
                    matrix[0][j] = 0
                elif grid[0][j] == 0 and matrix[0][j - 1] == 1:
                    matrix[0][j] = 1
            for n in range(1, y):
                for m in range(1, x):
                    if grid[n][m] == 0:
                        matrix[n][m] = matrix[n - 1][m] + matrix[n][m - 1]
                    else:
                        matrix[n][m] = 0
            return matrix[-1][-1]

print(a([[0,0],[1,1],[0,0]]))