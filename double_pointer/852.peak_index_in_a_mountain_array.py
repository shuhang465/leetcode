class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left+(right - left) // 2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return low
