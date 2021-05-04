# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 请判断一个链表是否为回文链表。
class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""		
		if not (head and head.next):
			return True
		arr = []
		# 申请一个数组，然后把元素都放到数组中
		while head:
			_,head = arr.append(head.val),head.next
		i,j = 0, len(arr)-1
		# 用i和j两个指针，一个往后，一个往前，不断迭代
		# 如果i的值不等于j说明不是回文，反之是回文
		while i<j:
			if arr[i]!=arr[j]:
				return False
			i,j = i+1,j-1
		return True
