# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left)//2
            if isBadVersion(mid) is False and isBadVersion(mid + 1) is True:
                return mid + 1
            elif isBadVersion(mid) is False:
                left = mid + 1
            elif isBadVersion(mid) is True:
                right = mid - 1
            
