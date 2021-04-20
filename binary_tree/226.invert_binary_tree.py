# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# 递归函数的终止条件，节点为空时返回
		if not root:
			return None
		# 将当前节点的左右子树同时交换
		root.left,root.right = root.right,root.left
		# 递归交换当前节点的 左子树和右子树
		self.invertTree(root.left)
		self.invertTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了		
		return root
