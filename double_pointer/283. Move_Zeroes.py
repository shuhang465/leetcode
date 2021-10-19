#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#快慢指针，一个驻守，一个开拓疆土，快指针开拓疆土，慢指针驻守
class Solution:
    
    def moveZeroes(self, nums: List[int]) -> None:
        #最开始都在营地
        fast , slow = 0,0
        while fast<len(nums):
            #快指针找到0之后就让慢指针驻守在0处，然后它取去找1，如果一直是1，那快慢一起移动，慢指针的职责就是跟随1移动，驻守0
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow+=1
            fast += 1
