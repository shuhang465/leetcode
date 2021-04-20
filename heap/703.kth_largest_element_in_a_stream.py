class KthLargest(object):

    def __init__(self, k, nums):
      
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val):
        
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]
