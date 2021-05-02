
class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		a,b = headA,headB
		# 定义了两个节点a和b，只要a和b不等就继续遍历
		while a!=b:
			# 这步很关键，请对照动态图配合理解，
			#当a的下一个为空时，就a就从b链表头开始遍历
			a = a.next if a else headB
			# 同理，b也是类似的
			b = b.next if b else headA
		return a


# 这道题其实跟 141.环形链表 有点类似，环形链表中题目已经明确说链表是有环的。而这道题只是说了两个链表有相交的节点，那么我们可以改变一下链表的结构，人为的将这个链表变成环形。
# 我们可以将a和b两个链表强行串联起来，变成一个8字的形状。我们将b链表的尾巴指向a节点的头部，将a节点的尾巴指向b链表的头部.然后我们定义两个指针，一个从a链表头出发，一个从b链表头出发，
# 因为是环形的，最终两个链表会相遇，而相遇的节点就是相交的节点

# 当两个链表没有相交点时不会陷入死循环嘛
# a执行完后，是先变成null，第二次再执行才指向headB的。 所以当两个链表一样长的时候，一趟遍历完就结束了，如果不一样长，就会遍历len(a)+len(b)次后，循环也就结束了
