# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
#拿到所有值之后再看，时间复杂度是O(N),因为每个节点遍历一次，空间复杂度O(N)，因为存储了中序遍历的结果，改进：只保留上一个节点，不保存所有遍历结果
class Solution(object):
  def inOrder(self, root):
    if not root:
      return []
    left = self.inOrder(root.left)
    right = self.inOrder(root.right)
    return left + [root.val] + right
  
  def isValidBST(self, root):
    inOrderList = self.inOrder(root)
    for i in range(len(inOrderList)-1):
      if inOrderList[i] >= inOrderList[i+1]:
        return False
    return True
