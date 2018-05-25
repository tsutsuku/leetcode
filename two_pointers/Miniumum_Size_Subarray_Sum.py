#Question No.209 Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Mine Solution , not elegant
        # total = i = j = 0
        # p = []
        # while j < len(nums):
        #     total += nums[j]
        #     j += 1
        #     if total >= s:
        #         while i < j:
        #             total -= nums[i]
        #             i += 1
        #             if total < s:
        #                 break
        #         if len(p) == 0 or j - i + 1 < p[1] - p[0]:
        #             p = [i - 1, j]
        # if len(p) > 0:
        #     return p[1] - p[0]
        # else:
        #     return 0

        # Office Solution
        i = j = total = 0
        l = 999999
        while j < len(nums):
            total += nums[j]
            j+= 1
            while total >= s:
                l = min(l, j- i)
                total -= nums[i]
                i += 1
        return 0 if l == 999999 else l

nums = [2,3,1,2,4,3]
s = 7
print(Solution().minSubArrayLen(s, nums))