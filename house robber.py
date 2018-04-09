import copy


class Solution:
    def rob(self, nums):
        # max_top = 0
        # max_second = 0
        # for i in range(len(nums)):
        #     num = nums[i]
        #     temp_second = max_top
        #     if num + max_second > max_top:
        #         max_top = num + max_second
        #     max_second = temp_second
        #
        # if max_top > max_second:
        #     return max_top
        # else:
        #     return max_second

        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now



nums = [4,1,2,7,5,3,1]
print(Solution().rob(nums))
