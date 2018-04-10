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
<<<<<<< HEAD
        if not head or not head.next:
            return head
        s = ListNode(0)
        n = head
        s.next ,p = n , n.next
=======
        s = n = ListNode(0)
        e = m = ListNode(0)
        s.next = p = head
>>>>>>> 5cb95c0afe1298c272d8c4f5d108808d95e0ce27
        while p:
            if p.val < x:
                n, p = n.next, p.next
            else:
                n.next = p.next
                m.next = p
                m = m.next
                p = n.next

        m.next = None
        n.next = e.next
        return s.next

<<<<<<< HEAD
s = [1,2]
=======
s = [2,1]
>>>>>>> 5cb95c0afe1298c272d8c4f5d108808d95e0ce27
node = ListNode(s[0])
d = node
for i in range(1, len(s)):
    node.next = ListNode(s[i])
    node = node.next

Solution().partition(d, 3)