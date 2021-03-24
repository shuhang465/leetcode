# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针,原地删除【0012233】
        # 最开始时快慢指针都在第一个位置，相等，当fast=slow时，快指针向前走【001】（走到1）
        # 当fast不等于slow时，slow往前走并且取值fast的值，【01】【1】
        # fast再往前，【0012】（走到2），slow=[012]
        #加一个特判
        if not nums:
            return 0
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1
