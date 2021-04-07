"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.append(root)
        level=1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for i in node.children:
                    if i is not None:
                        queue.append(i)
            level += 1

        return level-1

