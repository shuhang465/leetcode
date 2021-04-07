# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root):
        list_in = []
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        res = inorder(root)

        ans = cur = TreeNode(None)
        for i in res: 
            cur.right = TreeNode(i)
            cur = cur.right
        return ans.right


