from typing import List

def minFallingPathSum( matrix: List[List[int]]) -> int:
    n = len(matrix)
    mass = [[0] * n for _ in range(n)]
    if n == 1:
        return matrix[0][0]
    else:
        for i in range(n):
            mass[0][i]  = matrix[0][i]

        for i in range(n):
            for j in range(n):
                if j == 0:
                    mass[i][j] = min(mass[i-1][j], mass[i-1][j+1]) + matrix[i][j]
                elif j == n - 1:
                    mass[i][j] = matrix[i][j] + min(mass[i-1][j], mass[i-1][j-1])
                else:
                    mass[i][j] = matrix[i][j] + min(mass[i-1][j], mass[i-1][j+1], mass[i-1][j-1])
        answer = 1000000
        for i in range(n):
            answer = min(answer, mass[-1][i])
        return answer



print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))