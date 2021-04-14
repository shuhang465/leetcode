class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: 
            return 0
        sell, buy = [0] * (k+1), [-prices[0]] * (k+1)
        for price in prices[1:]:
            #这层循环是买卖的次数，最多买卖k次，所以到k+1
            for i in range(1, k + 1):
                #第i次买可以不动，那就是还是第i次买，或者买入
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], price + buy[i])
        print(sell)
        return sell[-1]
