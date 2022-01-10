# 街上有 n 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 0 开始且长度为 n 的整数数组 colors ，其中 colors[i] 表示第  i 栋房子的颜色。

# 返回 两栋 颜色 不同 房子之间的 最大 距离。

# 第 i 栋房子和第 j 栋房子之间的距离是 abs(i - j) ，其中 abs(x) 是 x 的绝对值。


class Solution(object):
    def maxDistance(self, colors):
 
        l = 0
        r = len(colors)-1

        if colors [r] != colors [l]:
            return (abs(r-l))
        else:
            while l < len(colors)-1 and colors[l] == colors[l+1]:
                l=l+1
                
                
            while r > 0 and colors[r] == colors[r-1]:
                r = r-1
            
            # [4,4,4,11,4,4,11,4,4,4,4,4]
            return max(len(colors)-l-2,(r-1))
