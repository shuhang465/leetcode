给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。

回想一下：

叶节点 是二叉树中没有子节点的节点
树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 从根节点出发开始寻找，不断向其较高的那部分子树前进，直到左右两边高度相同，该节点即为所求
class Solution:
    def deep(self, tree): #计算树的深度
        if tree == None:
            return 0
        return max(self.deep(tree.left), self.deep(tree.right)) + 1

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root.left == None and root.right == None:   
            return root
        left_deep = self.deep(root.left)
        right_deep = self.deep(root.right)
        if left_deep == right_deep:
            return root
        else:
            #如果左节点达到最深高度，右节点没有的话那这个根节点就不能算是最深节点的根结点
            return self.subtreeWithAllDeepest(root.left) if left_deep > right_deep else self.subtreeWithAllDeepest(root.right)


