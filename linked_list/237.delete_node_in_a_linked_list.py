# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# 刚看这个代码有点奇怪，不是要删除链表中一个节点吗，按理应该要传入两个参数，一个链表，一个节点，怎么只传入了一个参数，要删除的节点？
# 看了评论才发现node就是要删除的节点，我们任务是要把他删掉。但是不得不说leetcode的题目可读性太差了，给答题者造成歧义、不知道在说什么和误解都不是一个好题目，然而这些在leetcode简直太常见了
# 回到题目本身：
# 虽然我们不能delete这个node A，但可以用后面的node B把这个node覆盖掉，然后用它的下下个地址node C来作为node A的下一个地址。但是这个题越想越细思极恐щ(ʘ╻ʘ)щ，后背发凉！！
# 我们干掉的其实不是这个node A，而是它的下一个node B，我们本想杀掉的node正披着它的下一个node的外衣活着


