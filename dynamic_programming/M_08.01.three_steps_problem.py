class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, n):
            dp[i] = dp[i - 1]% 1000000007  + dp[i - 2] % 1000000007 + dp[i - 3]% 1000000007
            dp[i] = dp[i] % 1000000007 
        return dp[n-1] 
#动态规划思想是希望连续的，也就是说上一个状态和下一个状态(自变量)之间有关系而且连续。
#dp[i]：表示爬到第 ii 阶楼梯所有的上楼的方式。
#当爬第 ii 个阶梯时，有可能是从第 i - 1i−1 个阶梯爬上来的（选择只爬一层）；也有可能是从第 i - 2i−2 个阶梯爬上来的（选择爬两层）；还有可能是从第 i - 3i−3 个阶梯爬上来的（选择爬三层）。
#状态转移方程：dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
