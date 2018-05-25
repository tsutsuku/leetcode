#Question No.300 Longest Increasing Subsequence
#Url:https://leetcode.com/problems/longest-increasing-subsequence/solution/
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Basic Solution
        # d = []
        # lis = 0
        # for ni, nv in enumerate(nums):
        #     m = 1
        #     for k in range(len(d)):
        #         if nv > nums[k]:
        #             m = max(m, d[k] + 1)
        #     d.append(m)
        #     lis = max(lis, m)
        # return lis

        # Good Solution
        d = [int] * len(nums)
        l = 0
        for num in nums:
            i = bisect_left(d, num, 0, l)
            d[i] = num
            if i == l:
                l += 1
        return l



s = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(s))