# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#这道题只用返回和为k的数组的个数，所以可以用前缀和，[1,0,1,1,1] k=2,前缀和为[1,1,2,3,4]，pre_sum-k如果在前缀和集合里的话，就说明之前
#有数组和是2，比如3-2=1，然后前缀和是1的情况有两种，那就说明有两种情况数组和为2
#这里用defaultdict防止key不存在的时候引发keyerror异常
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      res = 0
      sum_count = collections.defaultdict(int)
      sum_count[0] = 1
      pre_sum_cur = 0
      for i in range(len(nums)):
          pre_sum_cur += nums[i]
          if pre_sum_cur - k in sum_count:
              res += sum_count[pre_sum_cur - k]
          sum_count[pre_sum_cur] += 1
      return res
#时间复杂度O(n),空间复杂度O(n)
