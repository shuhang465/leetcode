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
        if not root.left and not root.right:
            res.append(root.val)
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)

