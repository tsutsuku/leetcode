# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dict = {}
#         for i in range(len(nums)):
#             dict[nums[i]] = i
#
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in dict.keys() and dict[complement] != i:
#                 return [i, dict[complement]]
#
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in dict.keys():
#                 return [dict[complement], i]
#             dict[nums[i]] = i
#
# nums = [2, 2, 7, 15]
# target =  4
# print(Solution().twoSum(nums, target))