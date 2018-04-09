# Question No.75 Sort Colors
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Mine Solution
        # i, l, r = 0, 0, len(nums) - 1
        # while i <= r:
        #     while l <= i and i <= r and nums[i] != 1:
        #         if nums[i] == 0:
        #             nums[i], nums[l] = nums[l], nums[i]
        #             l += 1
        #         elif nums[i] == 2:
        #             nums[i], nums[r] = nums[r], nums[i]
        #             r -= 1
        #     i += 1

        # Office Solution
        l, r = 0, len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 2 and i < r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            while nums[i] == 0 and i > l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1


s = [2, 1]
Solution().sortColors(s)
print(s)
