# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#二叉树的层序遍历，返回按层遍历得到的节点值
#层序遍历和BFS要求的输入结果是不同的，层序遍历要求区分每一层就返回一个二维数组，而BFS的遍历结果是一个一维数组，无法区分每一层

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            #注意tmp变量的位置是写在while里面
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res


			

