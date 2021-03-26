class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        p, index = 0, 0
        while p < len(nums):
            if nums[p] != index:
                return index
            p += 1
            index += 1
        #最后这一步是判断最开始的值是0的时候的情况
        return index

