#给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #return sorted(num * num for num in nums)
        #因为是升序排列的，所以按照函数图像，平方最大值肯定处在函数的两侧
        n = len(nums)
        ans = [0] * n
        #这里加了一个pos变量，不断的为pos位置赋值，就是不断的通过比较左右两端的大小,同时更新三个值
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
