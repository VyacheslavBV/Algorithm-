from typing import List

def maximalSquare( matrix: List[List[str]]) -> int:
    m = len (matrix)
    n = len (matrix[0])

    if m == 1 and n == 1:
        if matrix[0][0] == "1":
            return 1
        else:
            return 0

    elif m == 1 and n > 1:
        flag = False
        for i in range(n):
            if matrix[0][i] == "1":
                flag = True
            if flag == True:
                return 1
            else:
                return 0

    elif m > 0 and n == 1:
        flag = False
        for i in range(m):
            if matrix[i][0] == "1":
                flag = True
            if flag == True:
                return 1
            else:
                return 0

    else:
        summ = 0
        for i in range(m):
            for j in range(n):
                print("вход на проверку числа")
                if matrix[i][j] == "0":
                    pass
                else:
                    summ = max(1, summ)
                    count = 1
                    for k in range(j + 1, n):
                        if matrix[i][k] == "1":
                            count += 1
                            if count <= m - i:
                                w = 0
                                for l in range(i,count):
                                    for p in range(j, count):
                                        w += int(matrix[l][p])
                                if w == count ** 2:
                                    summ = max(summ, w)
                                else:
                                    break
                            else:
                                break
                        else:
                            break
        return summ
print(maximalSquare([["0","0"],["1","1"],["1","1"]]))