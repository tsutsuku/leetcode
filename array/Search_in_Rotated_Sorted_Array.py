# Question No.33 Search in Rotated Sorted Array
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Mine Solution
        # if len(nums) == 0:
        #     return -1
        # mid = (int)(len(nums) / 2)
        # if len(nums) == 1:
        #     if nums[mid] == target:
        #         return 0
        #     else:
        #         return -1
        #
        # if (nums[0] <= nums[mid -1] and target >= nums[0] and target <= nums[mid - 1]) or(nums[0] > nums[mid -1] and (target >= nums[0] or target <= nums[mid -1])):
        #     left, right = 0, mid
        # else:
        #     left, right = mid, len(nums)
        # index = self.search(nums[left:right], target)
        # if index > -1:
        #     return index + left
        # else:
        #     return -1

        # Goods Solution
        # lo, hi = 0, len(nums) - 1
        # while lo < hi:
        #     mid = (int)((lo + hi) / 2)
        #     if (nums[mid] > nums[hi]):
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # rot = lo
        #
        # lo, hi = 0, len(nums) - 1
        # while lo <= hi:
        #     mid = (int)((lo + hi) / 2)
        #     real_mid = (mid + rot) % len(nums)
        #     if (nums[real_mid] == target):
        #         return real_mid
        #     if (nums[real_mid] < target):
        #         lo = mid + 1
        #     else:
        #         hi = mid - 1
        # return -1

        # Wonderful Solution
        lo, hi = 0, len(nums)
        while (lo < hi):
            mid = (int)((lo + hi) / 2)

            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            elif target < nums[0]:
                num = -9999
            else:
                num = 999

            if num < target:
                lo = mid + 1
            elif num > target:
                hi = mid
            else:
                return mid
        return -1




s = [4, 5, 6, 7, 0, 1, 2]
print(Solution().search(s, 0))
