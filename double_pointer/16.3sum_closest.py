class Solution(object):
    def threeSumClosest(self, nums, target):
        M = float("inf")    # 三个数的和初步设置为最大值
        lens = len(nums)
        nums.sort()         # 排序
        for i in range(lens):
            if i>0 and nums[i]==nums[i-1]:     #如果nums[i]的值相等，则跳过
                continue
            left = i + 1
            right = lens -1
            while left < right:
                ans = nums[i] + nums[left] + nums[right]
                if target == ans:
                    return target

                    #如果差值更接近，则保存差值更接近的三个数的和
                if abs(ans - target) < abs(M-target):   
                        M = ans
                
                if target  > ans:    #target太大，说明左边的值需要往右边移动来靠近target
                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    left += 1
    
                elif target < ans:    #target太小，说明右边的值需要往左边移动变小来靠近target
                    while left<right and nums[right]==nums[right-1]:
                        right -= 1
                    right -= 1

        return M
