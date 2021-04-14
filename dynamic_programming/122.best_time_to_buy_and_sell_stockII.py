class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        f = [[-prices[0], 0]] + [[0] * 2 for _ in range(n-1)]
       #f[i][0]表示手上持有股票的最大收益
       #f[i][1]表示手上不持有股票的最大收益
        for i in range(1, n):
            #可以是昨天持有股票或者是今天买的
            f[i][0] = max(f[i-1][0], f[i-1][1]-prices[i])
            #可以是昨天不持有股票的收益或者是昨天有股票今天卖了
            f[i][1] = max(f[i-1][1], f[i-1][0]+prices[i])
        return f[n-1][1]
