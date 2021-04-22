#魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，
# 若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
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
