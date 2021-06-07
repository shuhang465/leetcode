# 给你一个整数数组 nums，请你将该数组升序排列。
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快速排序
        def quick_sort(start, end):
            # 只剩一个元素时，不用再进行排序
            if start >= end: return
            # 任意找到个基准放到前面
            idx = random.randint(start, end)
            nums[start], nums[idx] = nums[idx], nums[start]
            pivot = nums[start]
            l, r = start, end
            while l < r:
                # 从右向左找到小的
                while l < r and nums[r] >= pivot:
                    r -= 1
                # 从左向右找到大的
                while l < r and nums[l] <= pivot:
                    l += 1
                #现在找到右面小的左面大的，这样又符合左小右大了
                nums[l], nums[r] = nums[r], nums[l]
            # 确定基准点的位置
            nums[start], nums[l] = nums[l], nums[start]
            quick_sort(start, l-1)
            quick_sort(l+1, end)
        
        quick_sort(0, len(nums) - 1)
        return nums
时间复杂度最好是每次都等分O(nlogn),最差是O(n2)
