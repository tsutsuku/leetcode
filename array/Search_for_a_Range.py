# Question No.34 Search for a Range
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Mine Solution
        #     if (len(nums) == 0):
        #         return [-1, -1]
        #     lo, hi = 0, len(nums) - 1
        #     while (lo < hi):
        #         mid = (int)((lo + hi) / 2)
        #         if nums[mid] < target:
        #             lo = mid + 1
        #         elif nums[mid] > target:
        #             hi = mid - 1
        #         else:
        #             return [lo + self.search(nums[lo:mid + 1], target, False),
        #                     mid + self.search(nums[mid:hi + 1], target, True)]
        #
        #     if (lo >= hi):
        #         if target == nums[lo]:
        #             return [lo, lo]
        #         else:
        #             return [-1, -1]
        #
        # def search(self, nums, target, big):
        #     lo, hi = 0, len(nums) - 1
        #     while (lo < hi):
        #         mid = (int)((lo + hi) / 2)
        #         if big:
        #             if nums[mid] <= target:
        #                 lo = mid + 1
        #             else:
        #                 hi = mid - 1
        #         else:
        #             if nums[mid] < target:
        #                 lo = mid + 1
        #             else:
        #                 hi = mid - 1
        #     if target == nums[lo]:
        #         return lo
        #     elif big:
        #         return lo - 1
        #     else:
        #         return lo + 1

        # Office Solution [more clean]
        lo, hi = 0, len(nums) - 1
        ret = [-1, -1]
        while lo < hi:
            mid = (int)((lo + hi) / 2)
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        if nums[lo] != target:
            return ret
        else:
            ret[0] = lo

        while lo < hi:
            mid = (int)((lo + hi) / 2)
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        ret[1] = hi
        return ret


s = [5, 7, 7, 8, 9, 10]
print(Solution().searchRange(s, 5))
