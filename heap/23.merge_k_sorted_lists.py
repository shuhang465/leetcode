# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 维护一个小顶堆，首先将所有链表的第一个节点加入小顶堆，
#每次从小顶堆中弹出一个节点node加入到最终结果的链表里，并将node的next加入到小顶堆中。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#维护一个小顶堆，首先将所有链表的第一个节点加入小顶堆，
#每次从小顶堆中弹出一个节点node加入到最终结果的链表里，并将node的next加入到小顶堆中。
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #如果链表数组是空的则直接返回
        if not lists:
            return None

        #建立一个堆，存入len(lists)个元素先，也就是把这几条链表的首个元素存入
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                #存的时候存链表的值还有是哪条链表
                heapq.heappush(heap, (lists[i].val, i))
                #然后指针往后挪
                lists[i] = lists[i].next

        #建立一个空的链表，存排序的元素
        dummy = ListNode()
        cur = dummy
        #然后不断的把链表里的值存在堆里，pop出最小值，存在新的链表里
        while heap:
            val, idx = heapq.heappop(heap)
            #新链表存的值就是pop出来的字典的值
            cur.next = ListNode(val)
            #链表指向下一个
            cur = cur.next
            #现在堆顶的那个元素pop出去了，再push进去对应链表的下一个值
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                #然后对应的链表指针往后指
                lists[idx] = lists[idx].next
        return dummy.next



# 时间复杂度：O(NlogK)，K是原始链表的数量，N是所有链表中的节点总数。堆操作是O(logK)，需操作N次。
# 空间复杂度：O(N+K)，N是节点总数，K是堆大小。

