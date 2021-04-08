class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 3:
            return ans
        nums.sort()
        # 如果最小的三个数已经大于 0，退出程序
        if nums[0] + nums[1] + nums[2] > 0:
            return []
        elif nums[-1] + nums[-2] + nums[-3] < 0:
            return []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 双指针
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                # 如果三数之和等于 0，
                if three_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 去除重复的左边元素
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 去除重复的右边元素
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # 更新 left， right的值
                    left += 1
                    right -= 1
                # 如果三数之和小于 0
                elif three_sum < 0:
                    left += 1
                # 如果三数之和大于 0
                else:
                    right -= 1
        return ans
