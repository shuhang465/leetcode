from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones) > 0:
            y = -heappop(stones)
            if len(stones) == 0:
                return y
            x = -heappop(stones)
            if x != y:
                heappush(stones, x - y)
        return 0
#正常每一次排序都需要O(nlogn)的时间复杂度，python有一个自带的heapq能创建小顶堆，我把数据变成负数就间接实现了大顶堆。
