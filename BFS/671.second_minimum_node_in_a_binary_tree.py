# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        #没有左右节点的话就顶多只有一个值，没有第二小值，所以返回-1
        if not root.left and not root.right:
            return -1
        from collections import deque
        queue = collections.deque()
        queue.append(root)
        nums = []
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                nums.append(node.val)
                if node.left:
                    queue.append(node.left)
                    #因为题目说每个节点的子节点的数量只能为0和2，所以不用加对右节点的判断
                    queue.append(node.right)
        minums = min(nums)

        res = 2**31
        for i in nums:
            if i > minums:
                res = min(res, i)
        return res if res != 2**31 else -1
