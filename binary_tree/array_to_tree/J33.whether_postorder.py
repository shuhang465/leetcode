# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
# [4, 8, 6, 12, 16, 14, 10]
#12大于10，break，分左右子树
# ([4, 8, 6, 12, 16, 14, 10], [4, 8, 6], [12, 16, 14])
# ([4, 8, 6], [4], [8])
# ([4], [], [])
# ([8], [], [])
# ([12, 16, 14], [12], [16])
# ([12], [], [])
# ([16], [], [])

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        #二叉搜索树的性质：
        #如果左子树不空，左子树的所有节点的值小于根节点的值。
        #如果右子树不空，则右子树所有节点的值大于跟节点的值。
        if postorder == []:return True
        n = len(postorder)
        for i in range(n):
            if postorder[i] > postorder[-1]:
                break
        left_tree = postorder[:i]
        right_tree = postorder[i:n-1]
        print(postorder,left_tree,right_tree)
        for num in right_tree:
            if num < postorder[-1]:
                return False
        return self.verifyPostorder(left_tree) and self.verifyPostorder(right_tree)   
