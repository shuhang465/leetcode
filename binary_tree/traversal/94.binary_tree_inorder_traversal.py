# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        l = self.inorder(root.left)
        r = self.inorder(root.right)
        return l + [root.val] + r

