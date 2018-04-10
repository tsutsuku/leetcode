#Question No.86 Partition List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        s = ListNode(0)
        n = head
        s.next ,p = n , n.next
        while p:
            if p.val < x:
                n.next = p.next
                s.next, p.next = p, s.next
                p = n.next
            else:
                n, p = n.next, p.next

        return s.next

s = [1,2]
node = ListNode(s[0])
d = node
for i in range(1, len(s)):
    node.next = ListNode(s[i])
    node = node.next

Solution().partition(d, 3)