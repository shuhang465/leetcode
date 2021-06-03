# 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

#这个题主要是说返回index最小的，所以当nums[mid]==target的时候，不能直接返回，要让right=mid,还有就是当nums[left]==target的时候直接返回left
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1
        left=0
        right=len(arr)-1
        while left < right:
            # 当left符合时直接返回, 因为找的是最小的索引
            if arr[left]==target:
                return left
            mid=left+(right-left)//2
            #当中间值等于目标值，将右边界移到中间，因为左边可能还有相等的值
            if arr[mid]==target:
                right=mid
            elif arr[left]<arr[mid]:
                #这里不要自己画个数组mid就直接和nums[0]比了，nums[mid]要和nums[left]比
                if arr[left]<=target<=arr[mid]:
                    right=mid
                else:
                    left=mid+1
            elif arr[left]>arr[mid]:
                if arr[mid]<=target<=arr[right]:
                    left=mid
                else:
                    right=mid-1
            else:
                    left+=1
        return left if arr[left] == target else -1

