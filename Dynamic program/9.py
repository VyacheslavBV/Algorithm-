from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] = grid[0][0]
        for i in range(x):
            matrix[i][0] = grid[i][0] + matrix[i-1][0]
        for j in range(y):
            matrix[0][j] = grid[0][j] + matrix[0][j-1]
        for k in range(1,y):
            for m in range(1,x):
                matrix[k][m] = grid[k][m] + min(matrix[k-1][m], matrix[k][m-1])


        return matrix[-1][-1]
him = Solution()
print(Solution.minPathSum(him, [[1,2,3]]))