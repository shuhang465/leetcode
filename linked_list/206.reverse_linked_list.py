# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
# 第二个指针 cur 指向 head，然后不断遍历 cur。
# 每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
# 都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		# 申请两个节点，pre和 cur，pre指向None
		pre = None
		cur = head
		# 遍历链表，while循环里面的内容其实可以写成一行
		# 这里只做演示，就不搞那么骚气的写法了
		while cur:
			# 记录当前节点的下一个节点
			tmp = cur.next
			# 然后将当前节点指向pre
			cur.next = pre
			# pre和cur节点都前进一位
			pre = cur
			cur = tmp
		return pre
