# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]


#这其实就是找规律
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        n=len(nums)
        # 向右移动的位置k可能会大于n，因此对n取余
        k=k%n
        if k==0 or n<2:
            return 
        # 以此为例：nums = [1,2,3,4,5,6,7], k = 3
        # 先整个数组反转：[7,6,5,4,3,2,1]
        reverse(0,n-1)
        # 前k个反转：[5,6,7,4,3,2,1]
        reverse(0,k-1)
        # 后n-k个反转：[5,6,7,1,2,3,4]
        reverse(k,n-1)
    


