#和之前用字典做法相比，这个数组是有序的，所以和木桶接水一样用双指针，比target大就往小的去，反之亦然
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left ,right = 0, len(numbers) - 1
        #两数之和，要有两个数，终止条件是左等于右这样就只有一个数了
        while left < right:
            if numbers[left] + numbers[right]  == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right]  < target:
                left += 1
            if numbers[left] + numbers[right]  > target: 
                right -= 1
