"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

#后续遍历二叉树时是先遍历左节点然后右节点，然后将根结点的值填入队列中
#N叉树则遍历所有子树之后再将根结点的值填入队列
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #保存节点值
        result = []
        #后序遍历
        def post_order(root):
            #跟节点非空入队列递归遍历
            if root:
                #递归遍历
                for node in root.children:
                    post_order(node)
                #节点值入队列
                result.append(root.val)
        post_order(root)
        return result
