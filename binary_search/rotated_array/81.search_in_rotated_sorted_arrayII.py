# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

#这道题有重复元素，查找元素是和nums[left]比，所以最后是left+1，找最小值是和nums[right]比，所以最后是right-1
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return True
            #寻找某个值的时候是和左比
            if nums[mid] < nums[left]:
                #先写好写的，剩下的else,如果target在有序的那一边的话则按下面操作
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            elif nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            #这里是left+1
            else:
                left += 1
        return True if nums[left] == target else False


