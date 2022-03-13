# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 计算给定二叉树的所有左叶子之和。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#bfs和dfs都可以
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return []
        res = 0
        from collections import deque
        queue = deque()
        queue.append(root)
        isLeafNode = lambda node: not node.left and not node.right
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    if isLeafNode(node.left):
                        res += node.left.val
                    else:
                        queue.append(node.left)
                if node.right:
                    if not isLeafNode(node.right):
                        queue.append(node.right)
        return res


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leafnode = lambda node: not node.left and not node.right 
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
                
        

