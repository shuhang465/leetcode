class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #全局变量
        left = 0
        right = len(nums)-1
        
        while left<=right:
            #mid是在里面变化的，局部变量
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    #写的时候想一下终止条件
