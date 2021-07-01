# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      s_map, t_map = {}, {}
      for c in s:
        if c in s_map:
          s_map[c] += 1
        else:
          s_map[c] = 1
      for c in t:
        if c in t_map:
          t_map[c] += 1
        else:
          t_map[c] = 1
      if s_map == t_map:
        return True
      else:
        return False
#如果直接sorted的话，时间复杂度是O(nlogn),空间复杂度是O(1)
#如果用哈希表的话，时间复杂度就变成O(n),空间复杂度变成O(n)
