#和69题很像
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

# 给定一个数字 n，找出可形成完整阶梯行的总行数。

# n 是一个非负整数，并且在32位有符号整型的范围内。

# n = 5

# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤

# 因为第三行不完整，所以返回2.

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
        return right
