class Solution:
    def addBinary(self, a, b) -> str:
        return '{:b}'.format(int(a, 2) + int(b, 2))

# 给你两个二进制字符串，返回它们的和（用二进制表示）。

# 输入为 非空 字符串且只包含数字 1 和 0。
