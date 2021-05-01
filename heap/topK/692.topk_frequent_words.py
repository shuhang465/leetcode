class Solution:
    def topKFrequent(self, words: List[int], k: int) -> List[int]:
        count = collections.Counter(words)
        heap = [(-val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nsmallest(k, heap)]
 
#2
# class Solution(object):
#     def topKFrequent(self, words, k):
#         count = collections.Counter(words)
#         heap = [(-freq, word) for word, freq in count.items()]
#         heapq.heapify(heap)
#         return [heapq.heappop(heap)[1] for _ in range(k)]


        
    
