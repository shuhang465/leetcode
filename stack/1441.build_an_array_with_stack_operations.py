class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for num in list(range(1,max(target)+1)):
            if num not in target:
                res.extend(["Push","Pop"])
            else:
                res.append("Push")
        
        return res

#注意extend和append
