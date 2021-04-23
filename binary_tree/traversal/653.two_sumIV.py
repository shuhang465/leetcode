# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def searchTree(root):
            if not root:return []
            return searchTree(root.left)+[root.val]+searchTree(root.right)
        
        arr=searchTree(root)
        l , r = 0, len(arr)-1
        while l < r:
            sum = arr[l] + arr[r]
            if sum == k:
                return True
            elif sum > k:
                r -= 1
            else:
                l += 1
            
        return False
