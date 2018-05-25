# Question No.378 Kth Smallest Element in a Sorted Matrix

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

s = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
print(Solution().kthSmallest(s, 8))
