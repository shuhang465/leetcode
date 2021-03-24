#这个比I还简单，不用判断中间的重复元素了
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        res = []
        nums1.sort()
        nums2.sort()
        while i<m and j<n:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res


        
