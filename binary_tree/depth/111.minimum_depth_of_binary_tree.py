# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(root):
            #注意这里返回的是0
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            # 只比计算树的高度110多了这一句话，就是说在返回高度的同时更新ans,这里的直径不是必须经过根结点的，所以是对所有节点遍历
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1
        depth(root)
        return self.ans - 1
