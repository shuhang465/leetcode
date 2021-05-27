# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
 #1.正常排序 时间复杂度O(nlogn) 空间复杂度O(logn)
class Solution:
  def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
      arr.sort()
      return arr[:k]
#2.堆，大根堆:建堆时间复杂度：O(k), 入堆和出堆操作的时间复杂度是O(logk),每个元素都要进行一次入堆操作，所以时间复杂度是O(nlogk), 小根堆O(nlogn)
#空间复杂度O(k), 因为大根堆里最多有k个数
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]]
        print(hp)
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                print(hp[0])
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans
#3.快速排序，时间复杂度期望O(n), 最坏情况下是O(n2)，最坏时每次的划分点都是最大值或者最小值，一共需要划分n-1次，而每一次划分需要线性的时间复杂度，所以是o(n2)
#空间复杂度的期望是O(logn),递归调用的期望深度是O(logn),每层需要的深度是O(1),只有常数个变量
#最坏的空间复杂度是O(n),最坏情况要划分n次，每层需要O(1)的空间，所以一共需O(n)的空间复杂度。
#但是数据量大的时候还是选择堆排序，因为快速排序需要修改原数组，如果原数组不能修改的话还要拷贝一份数组，空间复杂度就上去了
#而且快速排序需要保存所有的数据，当数据量非常大导致内存放不下的时候并不适合，而堆是来一个处理一个，不需要保存数据。
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k > len(arr) or k <= 0:
            return [] 
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k-1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low <high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low
