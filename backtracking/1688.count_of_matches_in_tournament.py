class Solution:
    def numberOfMatches(self, n: int) -> int:
        c = 0
        while n > 1:
            c += n // 2
            n = n // 2 + n % 2
                
        return c
