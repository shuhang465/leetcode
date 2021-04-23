# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


#直径最长不一定要经过根结点，直径等于某根节点左侧最深长度加右侧最深长度。
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

