# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right - left)//2
            #第一个要注意的地方：num(mid)和num(right)比，[7,8,9,0,1,2,3],0<3,所以最小值在mid左面[],但是[7,8,9,1,2],mid比7和2都大，所以无法判断最小值在哪里，所以mid要和右面的比
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            #第二个要注意的点是，这里是因为num(mid)可能会等于num(left)或者num(right)，比如[1,1,1,0,1]和[1,0,1,1,1],num(mid)都是1，但是这两种情况无法判断0在mid左边还是右边，
            #所以只能right不断的减1
            else:
                right -= 1
        #这里返回num(left)的原因是，最后的终止条件是[left,left),所以直接返回left
        return numbers[left]



       



