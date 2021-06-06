# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

# 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            #一个岛屿走向网格边界，周长加一
            if not 0 <= i < len(grid) or not 0 <= j <len(grid[0]) :
                return 1
            #一个岛屿走向水域，周长加一
            if grid[i][j] == 0:
                return 1
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            return (dfs(grid, i-1, j)+
            dfs(grid, i, j-1)+
            dfs(grid, i+1, j)+
            dfs(grid, i, j+1))
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
        return 0


        
