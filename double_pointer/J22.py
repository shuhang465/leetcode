# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #这个题使用双指针，最开始former和latter都指向head然后former开始往前挪，直到former和latter之间的距离等于k,然后former和latter同时向前挪动，直到former为空，这样latter指的就是倒数第k个点，时间复杂度为O(N)
        former, latter = head, head
        for _ in range(k):
            #如果former往前挪到了空，说明k>链表长度了，所以return
            if not former: return
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
