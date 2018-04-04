# Question No.27 Remove Element
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != val:
                nums.remove(nums[i])
        return len(nums)


s = [3, 2, 2, 3]
print(Solution().removeElement(s, 2))
