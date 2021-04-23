# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
class Solution:
    def increasingBST(self, root):
        list_in = []
        res = []
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return res
        res = inorder(root)
        ans = cur = TreeNode(None)
        for i in res: 
            cur.right = TreeNode(i)
            cur = cur.right
        return ans.right


