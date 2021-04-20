# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""		
		def dfs(r1,r2):
			# 如果 r1和r2中，只要有一个是null，函数就直接返回
			if not (r1 and r2):
				return r1 if r1 else r2
			# 让r1的值 等于  r1和r2的值累加
			# 再递归的计算两颗树的左节点、右节点
			r1.val += r2.val
			r1.left = dfs(r1.left,r2.left)
			r1.right = dfs(r1.right,r2.right)
			return r1
		return dfs(t1,t2)
