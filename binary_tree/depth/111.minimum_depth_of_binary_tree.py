# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def height(root:TreeNode):
            if not root:
                return 0
            L = height(root.left)
            R = height(root.right)
            if not root.left or not root.right:
                return max(L, R) + 1
            return min(L, R) + 1
        return height(root)


# [-9,-3,2,null,4,4,0,-6,null,-5]
#这个例子最小路径就是最右面那条，所以不是求完整体的左右树高度再取最小值，而是在算高度的时候就算好最小值
