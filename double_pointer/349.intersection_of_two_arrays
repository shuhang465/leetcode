#和合并有序数组差不多
#给定两个数组，编写一个函数来计算它们的交集。要求最后的交集没有重复值
#双指针，一个数组给一个指针
class Solution(object):
    def intersection(self, nums1, nums2):

        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0              # 设置双指针
        if not nums1 or not nums2:    # 如果有一个数组为空，则放回[]
            return []
        nums1.sort()              #排序
        nums2.sort()
        res = []
        while i < m and j < n:
            if nums1[i] == nums2[j]:      # 相等则保存值
                res.append(nums1[i])
                while i + 1 < m and nums1[i] == nums1[i + 1]:   # 跳过相同的值
                    i += 1
                while j + 1 < n and nums2[j] == nums2[j + 1]:   #  同上
                    j += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                while i + 1 < m and nums1[i] == nums1[i + 1]:
                    i += 1
                i += 1
            else:
                while j + 1 < n and nums2[j] == nums2[j + 1]:
                    j += 1
                j += 1
        return res
