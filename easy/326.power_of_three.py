给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 1:
            return True
        while n > 1:
            n = n/3
        return n == 1
    
    
