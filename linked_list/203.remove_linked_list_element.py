# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# 在head的前面增加一个节点。
# 从head开始循环：判断当前节点的下一个节点的值是否需要删除，需要删除则把next指向下一个节点。
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = head
        head = ListNode(None)
        head.next = tmp
        tmp = head
        while tmp and tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head.next

