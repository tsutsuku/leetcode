# Question No.31 Next Permutation
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Mine Solution
        # if len(nums) < 2:
        #     return
        #
        # for i in range(len(nums) - 1, 0, -1):
        #     if nums[i] > nums[i - 1]:
        #         imin = nums[i] - nums[i - 1]
        #         nmin = i
        #         for j in range(i, len(nums)):
        #             if nums[j] > nums[i - 1] and imin >= nums[j] - nums[i - 1]:
        #                 nmin = j
        #         nums[i - 1], nums[nmin] = nums[nmin], nums[i - 1]
        #         nums[i:] = sorted(nums[i:])
        #         return
        # nums.reverse()

        # Good Solution
        if len(nums) < 2:
            return
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i > 0:
            for j in range(i, len(nums)):
                if j == len(nums) - 1 or nums[j + 1] <= nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    break
        nums[i:] = reversed(nums[i:])

        # analysis：
        # in compare progress ,the compare result can be used for future compute

s = [5, 1, 1]

Solution().nextPermutation(s)
print(s)
