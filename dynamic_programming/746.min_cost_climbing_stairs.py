class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)      # 造楼梯顶
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
        return dp[-1]
