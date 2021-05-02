# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxVal = root.val
        def dfs( root ):
            if not root:
                return 0
            left = max( 0, dfs( root.left ) )
            right = max( 0, dfs( root.right ) )
            self.maxVal = max( self.maxVal,  root.val + left + right )
            return root.val + max( left, right )
        dfs(root)
        return self.maxVal

#路径每到一个节点，有 3 种选择：1. 停在当前节点。2. 走到左子节点。3. 走到右子节点。
#走到子节点，又面临这 3 种选择，递归就是用来处理这种规模不一样的相同问题。
# 定义dfs函数：返回当前子树能向父节点“提供”的最大路径和。即，一条从父节点延伸下来的路径，能在当前子树中获得的最大收益。分为三种情况：

# 路径停在当前子树的根节点，在这个子树中收益：root.val
# 走入左子树，在这个子树中的最大收益：root.val + dfs(root.left)
# 走入右子树，在这个子树中的最大收益：root.val + dfs(root.right)
# 对应了前面所讲，对父节点而言的三种选择，最大收益取最大值：root.val + max(dfs(root.left), dfs(root.right))

# 再次提醒: 一条从父节点延伸下来的路径，不能走入左子树又掉头走右子树，不能两头收益，路径会重叠。

# 当遍历到null节点时，null 子树提供不了收益，返回 0。

# 如果某个子树 dfs 结果为负，走入它，收益不增反减，该子树应被忽略，杜绝选择走入它的可能，让它返回 0，像null一样如同砍掉
