#给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

#因为二叉搜索树是左<中<右，所以
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        #这里ans使用的是局部变量，paths那里使用的是全局变量，而且不用return
        ans = 0
        dfs(root)
        return ans

