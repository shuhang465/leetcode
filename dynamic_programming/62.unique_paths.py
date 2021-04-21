class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 第一行都赋予 1
        for j in range(n):
            dp[0][j] = 1
        # 第一列都赋予 1    
        for i in range(m):
            dp[i][0] = 1
        # 两个for循环推导，对于(i,j)来说，只能由上方或者左方转移过来 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    

#这可能是路径转移类型动态规划最简单的一道题了
#对于每一个点，可能是从上方转移过来或者是从左方转移过来
