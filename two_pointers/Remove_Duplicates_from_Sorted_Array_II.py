# Question No.80 Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return len(nums)
        i = 1
        for j in range(2, len(nums)):
            if not (nums[j] == nums[i] and nums[j] == nums[i - 1]):
                i += 1
                nums[i] = nums[j]
        return i + 1

s = [1,1,1,2,2,3 ,3,4,4,4, 4,4]
print(Solution().removeDuplicates(s))
