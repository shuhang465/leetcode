# 给定一个整数 n，返回 n! 结果尾数中零的数量。
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        while n > 0:
            num += n // 5
            n = n // 5
        return num

