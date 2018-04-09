# Question No.25 Reverse Nodes in k-Group
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from queue import LifoQueue


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Mine Solution, Solved, speed not quick
        # p, n, q = head, 0, LifoQueue(maxsize=k)
        # s = e = ListNode(0)
        # while p:
        #     q.put_nowait(p)
        #     n, p = (n + 1) % k, p.next
        #     if not n:
        #         node = e.next = q.get_nowait()
        #         for _ in range(1, k):
        #             node.next = q.get_nowait()
        #             node = node.next
        #         e = node
        # node = None
        # while not q.empty():
        #     node = q.get_nowait()
        # e.next = node
        # return s.next

        p, n = head, 0
        while p and n != k:
            p = p.next
            n += 1
        if n == k:
            p = self.reverseKGroup(p, k)
            while n > 0:
                n -= 1
                e = head.next # e - next head in direct
                head.next = p # preappending "direct" head to the reversed list
                p = head # move head of reversed part to a new node
                head = e # move "direct" head to the next node in direct part
            head = p
        return head


s = [1, 2, 3]
node = ListNode(s[0])
d = node
for i in range(1, len(s)):
    node.next = ListNode(s[i])
    node = node.next
Solution().reverseKGroup(d, 2)
