# Question No.41 First Missing Positive
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Mine Solution
        # if len(nums) == 0:
        #     return 1
        #
        # nums.sort()
        # lo, hi = 0, len(nums) - 1
        # while lo < hi:
        #     mid = (lo + hi) // 2
        #     if (nums[mid] > 0):
        #         hi = mid
        #     else:
        #         lo = mid + 1
        #
        # i = lo
        # if nums[lo] == 1:
        #     while i < len(nums) - 1:
        #         if nums[i + 1] - nums[i] <= 1:
        #             i += 1
        #         else:
        #             break
        #
        # if i == lo and nums[i] != 1:
        #         return 1
        # else:
        #     return nums[i] + 1


        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                a = nums[i] - 1
                nums[i], nums[a] = nums[a], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


s = [-1,4,2,1,9,10]
print(Solution().firstMissingPositive(s))
