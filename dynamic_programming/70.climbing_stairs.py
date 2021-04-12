class Solution:
    # f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b



