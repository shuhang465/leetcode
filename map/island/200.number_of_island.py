# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, i, j):
            #终止条件是越界或者遇到了水
            if  not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
            #遍历完之后就让陆地变成0，这样避免重复遍历
            grid[i][j] = '0'
            #遍历该陆地的上下左右节点
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count
        


