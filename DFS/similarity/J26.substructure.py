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

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A and not B:
            return True
        elif not A or not B:
            return False
        return self.isSameTree(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
    def isSameTree(self, A,B):
        #最后终止条件是B便利完了就可以，不用AB所有值都相等，只要B所有节点在内相等就行，放宽一下条件
        if not B:
            return True
        elif not A or not B:
            return False
        elif A.val != B.val:
            return False
        return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)


    

    
   
    

