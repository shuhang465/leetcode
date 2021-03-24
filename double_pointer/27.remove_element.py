#移除元素
#给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

class Solution:
    #双指针，这里fast是一直往前走，移除重复元素时是fast==slow才往前走
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0,0
        if not nums:
            return None
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
