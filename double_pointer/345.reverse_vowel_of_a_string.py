class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        lst = list(s)
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            #这里要再加一个l<r的判断是因为，到最后剩下两个元素的时候，“，。”这样left加一，right减一，leftright的顺序就颠倒了，然后再次执行l+1,r-1就会out of range
            while l < r and lst[l] not in dic:
                l += 1
            while l < r and  lst[r] not in dic:
                r -= 1
            if l < r:
                lst[l], lst[r] = lst[r], lst[l]
            l = l + 1
            r = r - 1
          
    
        return ''.join(lst)
