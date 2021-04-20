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
        #res存的是最终结果，[[一层],[二层],[...]]
        res = []
	    #从collections里引入队列deque
        from collections import deque
        queue = deque()
	    #将跟节点放入队列中，不断遍历队列
        queue.append(root)
        while queue:
            #获取当前队列的长度，这个长度相当于这一层节点的个数
            size = len(queue)
            #注意tmp变量的位置是写在while里面
            tmp = []
            #对这一层的每个节点进行遍历，把每个节点拿出来存进list,然后把左右节点再放队列
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
