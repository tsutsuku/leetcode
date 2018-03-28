# Question No.2 Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Mine Solution()
        # l3 = None
        # start = None
        # next = 0
        # while l1 != None or l2 != None or next > 0:
        #     if l3 != None:
        #         l3.next = ListNode(0)
        #         l3 = l3.next
        #     else:
        #         l3 = ListNode(0)
        #         start = l3
        #
        #     if l1 == None:
        #         val1 = 0
        #     else:
        #         val1 = l1.val
        #         l1 = l1.next
        #
        #     if l2 == None:
        #         val2 = 0
        #     else:
        #         val2 = l2.val
        #         l2 = l2.next
        #
        #     l3.val = (val1 + val2 + next) % 10
        #     next = (val1 + val2 + next) // 10
        # else:
        #     l3.next = None
        #
        # return start


        # Good Solution()!
        d = ListNode(0)
        start = d
        sum = 0
        while l1 != None or l2 != None:
            sum //= 10
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            d.next = ListNode(sum % 10)
            d = d.next
        if sum // 10 == 1:
            d.next = ListNode(1)
        return start.next

s = [[2], [9, 9]]
w = []
for i in s:
    start = ListNode(0)
    node = start
    for j in i:
        node.val = j
        node.next = ListNode(0)
        node = node.next
    node = None
    w.append(start)

Solution().addTwoNumbers(w[0], w[1])
