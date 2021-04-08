class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            # ord()将char转化为对应的ASCⅡ码----大小写字母间相差32
            if stack and ((ord(stack[-1])-32) == ord(i) or (ord(stack[-1])+32) == ord(i)):
                stack.pop()
            else:
                stack.append(i)
        #list转为string
        return ''.join(stack)
