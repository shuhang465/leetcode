# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
# 就是考虑最下面的叶子连起来是不是一样的
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        if res1 == res2:
            return True
        return False

    def dfs(self, root, res):
        if not root:
            return
        #终止条件就是叶子，然后把叶子的值存起来
        if not root.left and not root.right:
            res.append(root.val)
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
