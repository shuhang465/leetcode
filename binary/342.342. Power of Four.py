# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

#解法： 二进制中的1只有一个，并且0的个数是2的倍数
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return bin(n).count('1') == 1 and bin(n).count('0') % 2 == 1 if n > 0 else False


