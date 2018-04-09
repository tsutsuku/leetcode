# Question No.19 Remove Nth node from end of list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Mine Solution, solved, but not so good
        # map = {}
        # i = 0
        # while head != None:
        #     map[i] = head
        #     head = head.next
        #     i += 1
        # if i - n > 0:
        #     map[i - n - 1].next = map[i - n].next
        #     return map[0]
        # elif 1 in map.keys():
        #     return map[1]
        # else:
        #     return None

        # Good Solution
        fast = slow =  head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


s = [1,2,3]
node = ListNode(s[0])
d = node
for i in range(1, len(s)):
    node.next = ListNode(s[i])
    node = node.next
Solution().removeNthFromEnd(d, 1)
