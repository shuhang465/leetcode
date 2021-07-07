# 给你一个整数数组 nums 和一个整数 k。
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
# 请返回这个数组中「优美子数组」的数目。
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        sum_count = collections.defaultdict(int)
        sum_count[0] =  1
        pre_sum_cur = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                pre_sum_cur += 1
            else:
                pre_sum_cur = pre_sum_cur
            if pre_sum_cur - k in sum_count:
                res += sum_count[pre_sum_cur - k]
            sum_count[pre_sum_cur] += 1
            print(pre_sum_cur)
        return res
#时间复杂度O(n),空间复杂度O(n)
