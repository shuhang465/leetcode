# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #和木桶里装最多水很像，双指针，最开始分别放在p1p2的最右侧，然后把大的值放在p1右侧，然后挪大的值
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        #这里就是说我在num1后面从最大值开始往前加，和977.x的平方根那道题有点像
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        #add missing elements from nums2，解决p2或者p1有一个为空的情况
        nums1[:p2 + 1] = nums2[:p2 + 1]
