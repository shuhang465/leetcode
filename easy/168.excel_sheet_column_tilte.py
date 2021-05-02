# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB 
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n:
            n -= 1
            #ASCII码转大写字符 并且左加 
            s = chr(65 + n % 26) + s
            print(s)
            n //= 26
        return s

