## Question No.26 Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Mine Solution
        # i = 0
        # if len(nums) > 0:
        #     while i < len(nums) - 1:
        #         while i < len(nums) - 1 and nums[i] == nums[i + 1]:
        #             nums.pop(i + 1)
        #         if i < len(nums) - 1:
        #             i += 1
        #     i += 1
        # return i

        # Office Solution
        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


s = [1, 1, 1]
print(Solution().removeDuplicates(s))
