class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        f = [[-prices[0],0]] + [[0] * 2 for _ in range(n-1)]
        for i in range(1, n):
            f[i][0] = max(f[i-1][0] , f[i-1][1] - prices[i]) 
            f[i][1] = max(f[i-1][1], f[i-1][0] + prices[i] - fee) 
        return f[n-1][1]
