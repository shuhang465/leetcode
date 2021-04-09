class Solution:

    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
            """
        dct = dict()
        s = s.split(" ")
        if len(s) != len(pattern): return False  #两个字符串长度不相同，返回False
        
        for i in range(len(pattern)):
            if pattern[i] not in dct:          # 如果pattern[i]不在字典中，此时要加入pattern[i]
                if s[i] in dct.values():       # 但是与dct[pattern[i]]对应的 s[i]却已经存在字典的值中，说明不是唯一映射
                    return False
                else:                            
                    dct[pattern[i]] = s[i]     # 如果s[i]还未存在，则加入新的映射
            else:
                if dct[pattern[i]] != s[i]:     # 如果pattern[i]在字典中了，但是dct[pattern[i]]的值不等于s[i]，说明已存在其他映射
                    return False
        return True


