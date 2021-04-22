class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b, c = 1, 1, 2
        for _ in range(n-2):
            a, b, c = b, c, a+b+c
            a = a % 1000000007
            b = b % 1000000007
            c = c % 1000000007
        return c 
