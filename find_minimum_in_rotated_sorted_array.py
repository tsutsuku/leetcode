# class Solution:
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # min = nums[0]
#         # for i in nums:
#         #     if i < min:
#         #         min = i
#         # return min
#
#         lo, hi = 0, len(nums)-1
#         while(lo < hi):
#             mid = (int)((lo + hi) /2)
#             if (nums[mid] > nums[hi]):
#                 lo = mid +1
#             else:
#                 hi = mid
#
#         return lo
#
# nums = [1]
# print(Solution().findMin(nums))