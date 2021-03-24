class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast , slow = 0,0
        while fast<len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow+=1
            fast += 1
