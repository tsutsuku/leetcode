# Question No.142 Linked List Cycle II
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ##Not find a Solution
        ##Office Solution
        # k = nr
        # s = k - m
        # s = nr - m = (n-1)r + (r-m)
        # assume n = 1
        if head == None or head.next == None:
            return None
        p = q = head
        cycle = False
        while p != None and q != None:
            p = p.next
            if q.next == None:
                return None
            q = q.next.next
            if p == q:
                cycle = True
                break
        if not cycle:
            return None
        p = head
        while p != q:
            p = p.next
            q = q.next
        return p
