# 最开始的想法是：我们对A中的结点去遍历，每个结点都调用之前写的 isSameTree，如果A中的某个结点和B完全一样，那不就找到了吗！
# 后来发现有个bug，就是 B不仅可以是 A的末端，也可以是中间的某段。（A可以比B 多一点分叉）
# 所以只要把isSameTree的条件放宽一点就好了：不需要完全相等，只要在B的所有结点内都相等就好了。
# isSameTree函数 放宽条件，改写成本文中的judge函数。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        if not A or not B:
            return False
        return self.judge(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def judge(self, A, B):
        if not B:
            # b都遍历完了，还没发现不一样的，说明那就一样了
            return True
        if not A:
            # 压根就没有a，当然不行
            return False
        if A.val!= B.val:
            # a b 的值不相等，肯定不行
            return False
        return self.judge(A.left,B.left) and self.judge(A.right, B.right)


    

    
   
    

