# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 计算给定二叉树的所有左叶子之和。
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        #判断是否为叶子结点
        def leafnode(root):
            if not root.left and not root.right:
                return True
            return False
        #深度优先遍历
        def dfs(root):
            if not root:
                return 0
            ans = 0
            #如果左子树存在
            if root.left:
                #判断是不是叶子节点
                if leafnode(root.left):
                    #是的话直接+val
                    ans += root.left.val
                else:
                    #不是的话继续dfs
                    ans += dfs(root.left)
            #如果右子树存在
            if root.right:
                #右节点是不是叶子节点，如果是，不判断，如果不是继续dfs
                if not leafnode(root.right):
                    #继续遍历右子树
                    ans += dfs (root.right)
            return ans
        return dfs(root)
                




