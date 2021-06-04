# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #终止条件：越过叶子节点直接返回null，root等于p或者q的话返回root
        if not root or root == p or root == q: 
            return root
        #递推：递推左右节点
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        #返回值：当左右同时为空说明root的左右子树都不包含pq,返回null
        #当left或者right不为空的时候，返回left或者right
        if not left: return right
        if not right: return left
        #当left和right同时不为空时返回root
        return root





