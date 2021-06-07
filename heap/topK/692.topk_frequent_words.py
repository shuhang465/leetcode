# 给一非空的单词列表，返回前 k 个出现次数最多的单词。
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

#次数多，用小根堆，然后按照次数pop出来就变成了从大到小的排列，但是，在排次数的时候是a:1, b:1(word和freq同时排序),pop的时候就是b,a,但是又要pop的时候按照字母表的顺序，所以就重写一个类
class WF:
    def __init__(self, w,  f):
        self.f = f
        self.w = w
    def __gt__ (self, other):   #重写 >
        if self.f > other.f or (self.f == other.f and self.w < other.w):
            return True
        return False
    # def __lt__(self,  other): #重写 <
    #     if self.f < other.f or (self.f == other.f and self.w > other.w):
    #         return True
    #     return False
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = collections.Counter(words)
        minHeap = []            #维持一个长度为k的最小堆，方便把当前最小的踢出去
        for w, f in word_freq.items():
            heapq.heappush(minheap, WF(w, f))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [heapq.heappop(minHeap).w for i in range(k)][::-1]


