class Solution(object):
#这道题主要是lower()和判断是否是字母和数字的问题，双指针没有很难。
    def not_letters_digits(self,c):
        return not 'a' <= c <= 'z' and not '0' <= c <= '9'
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        s = s.lower()
        while left < right:
            while left < right and self.not_letters_digits(s[left]):left+=1
            while left < right and self.not_letters_digits(s[right]):right-=1
            if s[left] == s[right]:
                left+=1
                right-=1
            else:return False
        return True
