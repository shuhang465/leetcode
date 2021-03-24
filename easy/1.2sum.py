#找到等于target的两个数
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[4, 5, 6] -> {4:0, 5:1, 6:2}, target=9
        #利用if key in dict,在的话则返回，不在的话则将值写入字典
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return d[target-nums[i]], i
            else:
                d[nums[i]] = i
