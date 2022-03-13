
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

# 返回这些数字之和。题目数据保证答案是一个 32 位 整数。

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
        #注意，dfs什么也没有返回，最后只是path的值发生了变化，所以后面要比较path
        print(paths)
        res = 0
        for s in paths:
            res += int(s, 2)
        return res
        
