class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + (right-left)//2
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid
        if left * left > x:
            return left-1
        else:
            return left
        
