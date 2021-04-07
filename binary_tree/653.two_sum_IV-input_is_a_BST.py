# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

