# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 树中节点数目在范围 [1, 25] 内
# 1 <= Node.val <= 231 - 1
# 对于树中每个节点 root.val == min(root.left.val, root.right.val)


#这道题就是层序遍历二叉树把值存起来，然后再找比最小值大的最小点
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        #因为前提是非空二叉树，所以没有左右节点的话就顶多只有一个值，没有第二小值，所以返回-1
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
                    #因为题目说每个节点的子节点的数量只能为0和2，所以有左一定有右，不用加对右节点的判断
                    queue.append(node.right)
        minums = min(nums)

        res = 2**31
        for i in nums:
            if i > minums:
                res = min(res, i)
        return res if res != 2**31 else -1
