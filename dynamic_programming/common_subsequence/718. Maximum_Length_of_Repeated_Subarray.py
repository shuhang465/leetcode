# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#这道题要求数组是连续的
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        ans = 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans


# dp[i][j]：表示第一个数组 A 前 i 个元素和数组 B 前 j 个元素组成的最长公共子数组(相当于子串)的长度。
# 我们在计算 dp[i][j] 的时候：
# 若当前两个元素值相同，即 A[i] == B[j]，则说明当前元素可以构成公共子数组，所以还要加上它们的前一个元素构成的最长公共子数组的长度(在原来的基础上加 1)，此时状态转移方程：dp[i][j] = dp[i - 1][j - 1] + 1。
# 若当前两个元素值不同，即 A[i] != B[j]，则说明当前元素无法构成公共子数组(就是：当前元素不能成为公共子数组里的一员)。因为公共子数组必须是连续的，而此时的元素值不同，相当于直接断开了，此时状态转移方程：dp[i][j] = 0。

