class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1 , m):
            for j in range(1 , n):
                grid[i][j] += min(grid[i][j-1] , grid[i-1][j])
        return grid[-1][-1]

#在矩阵中每一次只能向下或者向右移动一步。
#那么对于矩阵中某个位置grid[i][j]grid[i][j]，从左上角到它的路径之和就是这个位置上面或者左边位置路径的最小值，可以表示为grid[i][j] += min(grid[i][j-1] , grid[i-1][j])grid[i][j]+=min(grid[i][j−1],grid[i−1][j])。

