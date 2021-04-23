# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # 遍历就完事了
        if not root:
            return True
        if root.left:
            if root.left.val != root.val:
                return False
        if root.right:
            if root.right.val != root.val:
                return False
                
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
