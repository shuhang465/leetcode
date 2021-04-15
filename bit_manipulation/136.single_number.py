class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

#用异或运算，两个相同的得0，输出最后落单的那个
