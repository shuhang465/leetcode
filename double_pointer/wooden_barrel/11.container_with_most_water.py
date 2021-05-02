#给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

class Solution:
#双指针
#桶的左和右分别往里走，长的板子往里走面积不会变大，因为取min{左，右}*宽度
#所以长板往里走高度不会变大，因为取了min，所以就要让短板往里走，这样面积才有可能会变大
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
       
        while i < j:
            #哪边高度低哪边往里走
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
