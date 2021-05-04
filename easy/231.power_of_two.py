# 计算n的二进制的'1'的个数：
# 只有一个1说明是二的幂级数
# 例如：
# 0b10000为二的幂级数
# 0b10001``0b10011等都不可能是二的幂级数
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n).count('1') == 1 if n > 0 else False



