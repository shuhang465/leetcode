class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #这个题没有越界的问题，因为最大的那个字母比target小的话就直接返回letters[0]
        if letters[-1] <= target:
            return letters[0]
        left = 0
        right = len(letters)-1
        while left <= right:
            mid = left + (right-left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left]
