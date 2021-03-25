#和69题很像
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right-left)//2
            if (mid+1)*mid//2 == n:
                return mid
            if (mid+1)*mid//2 < n:
                left = mid + 1
            else:
                right = mid -1
        if (left+1)*left//2 > n:
            return left - 1
        else:
            return left
