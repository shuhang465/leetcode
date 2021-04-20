"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

#n叉树的层序遍历
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                #只有这里和二叉树不一样，而且是extend，如果用append的话就会【1，2，3【4，5，6】】这样
                if node.children:
                    queue.extend(node.children)
                
            res.append(tmp)
        return res


