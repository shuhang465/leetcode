class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        index = 0
        p = 0
        while p < len(nums):
            if index == nums[p]:
                return index
            p += 1
            index += 1
        return -1
