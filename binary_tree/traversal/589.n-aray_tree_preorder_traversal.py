"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #保存节点值
        result = []
        #前序遍历
        def pre_order(root):
            #跟节点非空入队列递归遍历
            if root:
                #节点值入队列
                result.append(root.val)
                #递归遍历
                for node in root.children:
                    pre_order(node)
        pre_order(root)
        return result
