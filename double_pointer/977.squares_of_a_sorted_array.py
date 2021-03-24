class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #return sorted(num * num for num in nums)
        #因为是升序排列的，所以按照函数图像，平方最大值肯定处在函数的两侧
        #故左右指针，左右往里靠
        n = len(nums)
        ans = [0] * n
        left , right , pos = 0, n-1, n-1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                ans[pos] = nums[left] * nums[left]
                left += 1
            else:
                ans[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return ans
