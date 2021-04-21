# 稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
#  输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
#  输出：-1
#  说明: 不存在返回-1。


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        #这道题注意是排好序的，所以可以用左右指针
        left,right=0,len(words)-1
        while left<=right:
            #首先pass掉空格
            while words[left]=='':
                left+=1
            while words[right]=='':
                right-=1
            #但是pass掉之后要判断是不是left还是小于right
            if left>right:
                break
            #然后再用二分查找
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
