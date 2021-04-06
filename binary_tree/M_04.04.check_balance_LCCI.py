# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#平衡二叉树就是看左右子树的高度差，所以要算左右树的高度
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #类里面写函数不用写self
        def height(root: TreeNode):
            #加一个特判
            if not root:
                return 0
            #返回左右树的最大高度加一
            return max(height(root.left), height(root.right)) + 1
        #加一个特判，如果是空树的话就直接是平衡的
        if not root:
            return True
        #注意后面要加上判断左右子树，因为大树高度一样，小树可能不一样[1223nn34nn4]
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
