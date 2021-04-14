class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            #f[i][0]可以是i-1的时候就持有的，也可以是i天买入的，那么i-1天就不能处于冷冻期
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            #f[i][1]表示前一天卖出股票，等于前一天的最大收益加上前一天卖股票得到的钱
            f[i][1] = f[i - 1][0] + prices[i]
            #f[i][2]表示昨天没有进行股票操作，也就是昨天没有任何股票，那这时就氛围昨天处于冷冻期还是非冷冻期
            f[i][2] = max(f[i - 1][1], f[i - 1][2])
        
        return max(f[n - 1][1], f[n - 1][2])
