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
# 如果某次哨兵划分后 基准数正好是第 k+1 小的数字 ，那么此时基准数左边的所有数字便是题目所求的 最小的 k 个数 
# 哨兵划分：
# 划分完毕后，基准数为 arr[i] ，左/右子数组区间分别为 [l, i - 1],[i + 1, r]；
# 递归或返回：
# 若 k < i ，代表第 k + 1 小的数字在左子数组中，则递归左子数组；
# 若 k > i ，代表第 k + 1 小的数字在右子数组中，则递归右子数组；
# 若 k = i，代表此时 arr[k] 即为第 k + 1小的数字，则直接返回数组前k个数字即可；

#但是数据量大的时候还是选择堆排序，因为快速排序需要修改原数组，如果原数组不能修改的话还要拷贝一份数组，空间复杂度就上去了
#而且快速排序需要保存所有的数据，当数据量非常大导致内存放不下的时候并不适合，而堆是来一个处理一个，不需要保存数据。
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr): return arr
        def quick_sort(start, end):
            l, r = start, end
            pivot = arr[start]
            while l < r:
                while l < r and arr[r] >= pivot: r -= 1
                while l < r and arr[l] <= pivot: l += 1
                arr[l], arr[r] = arr[r], arr[l]
            arr[start], arr[l] = arr[l], arr[start]
            #上面就是正常的快速排序，这里是递归
            if k < l: return quick_sort(start, l-1)
            if k > l: return quick_sort(l+1, end)
            return arr[:k]
        return quick_sort(0, len(arr)-1)

