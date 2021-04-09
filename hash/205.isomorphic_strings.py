class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = dict()
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            #if key in dict
            if t[i] not in dct:
                if s[i] in dct.values():
                    return False
                else:
                    dct[t[i]] = s[i]
            else:
                if dct[t[i]] != s[i]:
                    return False
        return True
