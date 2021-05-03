# 给定一个Excel表格中的列名称，返回其相应的列序号。
# A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0 
        for i in columnTitle:
            ans = ans*26+ord(i)-64
        return ans
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值

