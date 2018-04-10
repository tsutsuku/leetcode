# Question No.141 Linked List Cycle
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## Mine Solution
        # p = q = head
        # while p:
        #     p = p.next
        #     if q and q.next:
        #         q = q.next.next
        #     else:
        #         return False
        #     if p == q:
        #         return True
        # return False

        ##Office Solution
        if head == None or head.next == None:
            return False
        p = head
        q = head.next
        while p != q:
            if p == None or q.next == None:
                return False
            p = p.next
            q = q.next.next
        return True


s = [1, 2]
node = ListNode(s[0])
d = node
for i in range(1, len(s)):
    node.next = ListNode(s[i])
    node = node.next
Solution().hasCycle(d)
