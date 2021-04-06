# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.res=0
        def dfs(root):
            if not root:return 0
            p1= dfs(root.left)
            p2=dfs(root.right)
            #更新坡度差
            self.res+= abs(p1-p2)
            #返回坡度和，这里是为了后面父节点计算差的绝对值
            return p1+p2+root.val
        dfs(root)
        return self.res

