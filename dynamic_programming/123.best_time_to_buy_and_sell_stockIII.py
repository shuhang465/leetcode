class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==0:
            return 0
        buy_1 = buy_2 = float('inf')
        pro_1 = pro_2 = 0
        for p in prices:
            buy_1 = min(buy_1, p)
            pro_1 = max(pro_1, p - buy_1)
            buy_2 = min(buy_2, p - pro_1) # p - pro_1 是用第一次的钱抵消了一部分第二次买的钱
            pro_2 = max(pro_2, p - buy_2)
        return pro_2


