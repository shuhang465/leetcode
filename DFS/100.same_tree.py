# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#判断两棵树是否相同
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#两棵树都空则相同，有一棵空一棵不空或者根节点值不一样则不相同，然后对左1左2右1右2子树进行判断
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

