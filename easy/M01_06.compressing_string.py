
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
输入："aabcccccaaa"
输出："a2b1c5a3"
输入："abbccd"
输出："abbccd"
解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

    def compressString(self, S: str) -> str:
        if len(S) == 1 or len(S) == 0:
            return S
        tmp = 1
        re = S[0]
        for i in range(len(S) - 1):
            if S[i] != S[i + 1]:
                re = re + str(tmp)
                re = re + S[i + 1]
                tmp = 1
            else:
                tmp += 1
        re = re + str(tmp)
        if len(S) > len(re):
            return re
        else:
            return S
