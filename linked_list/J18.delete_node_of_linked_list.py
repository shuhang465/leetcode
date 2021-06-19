# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

# 返回删除后的链表的头节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#这个题主要是加了一个pre,只要先判断完head.val?=val之后，下一个cur就有pre了，如果cur.val一直不等于val,则一直往前，直到跳出循环（等于val或者cur==None了），然后pre的下一个指向cur的下一个
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head



