# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # 题目数组非空，
        # if not root:
        #     return []

        # 返回结果
        res = []

        from collections import deque
        queue = deque()
        # 将根节点入队
        #不管干啥，首先把root放到队列里，然后再对队列里的值进行pop
        queue.append(root)
        # 队列不为空，表达式二叉树还有节点，循环遍历
        while queue:
            # 先标记每层的节点数
            size = len(queue)
            # 定义变量，记录每次节点值
            total = 0
            # 这里开始遍历当前层的节点
            for _ in range(size):
                #出队
                node = queue.popleft()
                # 先将当前节点的值存储
                total += node.val
                # 节点的左右节点非空时，入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 添加每层的节点值均值
            res.append(total/size)
        return res
