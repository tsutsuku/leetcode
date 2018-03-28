# Question No.23 Merge k Sorted Lists
# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # Mine Solution, Time Limit exceeded
        # stack = []
        # for i in range(len(lists)):
        #     if lists[i] == None:
        #         continue
        #     for j in range(len(stack)):
        #         if lists[i].val < lists[stack[j]].val:
        #             stack.insert(j, i)
        #             break
        #     else:
        #         stack.append(i)
        #
        # if len(stack) == 0:
        #     return None
        #
        # d = ListNode(0)
        # s = d
        # while len(stack) > 0:
        #     index = stack.pop(0)
        #     d.next = lists[index]
        #     d = d.next
        #     node = lists[index].next
        #     lists[index] = node
        #     if node != None:
        #         for i in range(len(stack)):
        #             if node.val < lists[stack[i]].val:
        #                 stack.insert(i, index)
        #                 break
        #         else:
        #             stack.append(index)
        # return s.next

        # Good Solution
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue(maxsize=len(lists))
        for list_idx, node in enumerate(lists):
            if node:
                q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next


# s = [[]]
s = [[], [-1, 5, 11], [], [6, 10]]
w = []
for i in s:
    start = ListNode(0)
    node = start
    for j in i:
        node.next = ListNode(j)
        node = node.next
    node = None
    w.append(start.next)

Solution().mergeKLists(w)
