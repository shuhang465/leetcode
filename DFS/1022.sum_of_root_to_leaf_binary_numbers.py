# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    dfs(node.left, path)
                    dfs(node.right, path)
        paths = []
        dfs(root, '')
        print(paths)
        res = 0
        for s in paths:
            res += int(s, 2)
        return res
        
