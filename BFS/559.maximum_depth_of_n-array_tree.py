"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 给定一个 N 叉树，找到其最大深度。

# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

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

