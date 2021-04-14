class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif left < right and nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
