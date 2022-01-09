class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
       
        def count(e):
            return bin(e).count("1")

        arr.sort(key=lambda e: (count(e), e))
        return arr
