class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left,right=0,len(words)-1
        while left<=right:
            while words[left]=='':
                left+=1
            while words[right]=='':
                right-=1
            if left>right:
                break
            mid=left+((right-left)//2)
            while words[mid]=='':
                mid+=1
            if s==words[mid]:
                return mid
            elif s<words[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1
