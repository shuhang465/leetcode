# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。


#判断两个树是否相等的三个条件是与的关系，即：
# 当前两个树的根节点值相等；
# 并且，s 的左子树和 t 的左子树相等；
# 并且，s 的右子树和 t 的右子树相等。
# 而判断 t 是否为 s 的子树的三个条件是或的关系，即：
# 当前两棵树相等；
# 或者，t 是 s 的左子树；
# 或者，t 是 s 的右子树。

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        elif s.val != t.val :
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

