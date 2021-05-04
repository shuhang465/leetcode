# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(t))==sorted(list(s))
#直接排序后比较
