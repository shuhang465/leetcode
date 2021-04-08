class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(nums: List[int], n: int, target: int) -> List[List[int]]:
            res = []
            if len(nums) < n:
                return res
            if n == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == target:
                        res.append([nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
                return res
            else:
                for i in range(len(nums)-n+1):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    min_sum = sum(nums[i:i+n])
                    if min_sum > target:
                        break
                    max_sum = nums[i] + sum(nums[-n+1:])
                    if max_sum < target:
                        continue
                    sub_res = nSum(nums[i+1:], n-1, target-nums[i])
                    for j in range(len(sub_res)):
                        res.append([nums[i]]+sub_res[j])
                return res
        nums.sort()
        res = nSum(nums, 4, target)
        return res

