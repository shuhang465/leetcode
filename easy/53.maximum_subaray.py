
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur = -1000000, 0
        for i in range(len(nums)):
            cur = max(cur + nums[i], nums[i])
            ans = max(ans, cur)
        return ans
      

