class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
       
            if nums[mid] > nums[right]:
                left = mid + 1
            #这里和right比的原因是，[7,8,0,1,2,3,4],mid=1<left=7,这时不知道往left+1还是right-1
            elif nums[mid] < nums[right]:
                right = mid
            else:
            #这里是[1,0,1,1,1],[1,1,1,0,1],mid=1=left=right,无法判断左右
                right -= 1
        return nums[left]

