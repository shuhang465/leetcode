class Solution(object):
    def frequencySort(self, s):
        temp = set(s)

        # 保存为dict
        d = {}
        for i in temp:
            d[i] = s.count(i)

        # 对字典按照value排序
        s = sorted(d.items(), key = lambda x: x[1], reverse = True)
        res = ""
        # 结果整理
        for i in s:
            res += i[0] * i[1]

        return res
