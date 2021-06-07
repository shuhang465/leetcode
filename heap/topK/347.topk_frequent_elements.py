class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        nums = [(val, key) for key, val in count.items()]
        topKs = self.quick_sort(nums, k, 0, len(nums) - 1)
        return [item[1] for item in topKs]
    def quick_sort(self, nums,k, start, end):
        if k >= len(nums): return nums
        l, r = start, end
        pivot = nums[start][0]
        #这里要从大到小排，所以让pivot左边都比他大，右边都比他小
        while l < r:
            while l < r and nums[r][0] <= pivot: r -= 1
            while l < r and nums[l][0] >= pivot: l += 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[start], nums[l] = nums[l], nums[start]
        #上面就是正常的快速排序，这里是递归
        if k < l: return self.quick_sort(nums, k, start, l-1)
        if k > l: return self.quick_sort(nums, k, l+1, end)
        return nums[:k]


