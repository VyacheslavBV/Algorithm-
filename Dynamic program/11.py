from typing import List


def minimumTotal(triangle: List[List[int]]):
    ln = len(triangle)
    mass = [0] * ln
    k = 1

    if ln == 1:
        return triangle[0][0]
    else:
        for i in range(ln):
            k += 1
            mass[i] = [0] * k

        mass[0][0] = triangle[0][0]
        for i in range(1,ln):
            mass[i][0] = mass[i-1][0] + triangle[i][0]
        g = 0
        for i in range(1, ln):
            g += 1
            for j in range(1, len(triangle[g])):
                if j == len(triangle[g]) - 1 :
                    mass[i][j] = triangle[i][j] + mass[i - 1][ j-1]
                else:
                    mass[i][j] = triangle[i][j] + min(mass[i - 1][j - 1], mass[i - 1][j])

        answer = 10000

        for i in range(ln):
            answer = min(mass[-1][i], answer)
        return answer








print(minimumTotal([[1],[1,2]]))