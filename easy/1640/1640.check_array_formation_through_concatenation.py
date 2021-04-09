class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        ret = []
        for i in arr:
            for j in pieces:
                if i != j[0]:
                    continue
                ret.extend(j)
        
        return ret == arr
