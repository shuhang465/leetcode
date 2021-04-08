class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        if len(nums) < 4:
            return ans;
        nums.sort()
        length = len(nums)
        for i in range(length):
            if nums[i] > 0 and target < 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                two_sum = nums[i] + nums[j]
                if two_sum > 0 and target < 0:
                    break
                left, right = j + 1, length - 1
                while left < right:
                    four_sum = two_sum + nums[left] + nums[right]
                    # residual = target - nums[i] - nums[j] - nums[left] - nums[right]
                    if four_sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return ans
