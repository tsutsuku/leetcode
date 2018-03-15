##Question No.16 3Sum Closest

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Mine Solution
        # nums.sort()
        # i = 0
        # closest = -9999999
        # while i < len(nums) - 2:
        #     sum = nums[i] + nums[i + 1] + nums[i + 2]
        #     if sum > target:
        #         if abs(closest - target) < abs(sum - target):
        #             return closest
        #         else:
        #             return sum
        #
        #     imin, imax = i + 1, len(nums) - 1
        #     while (imin < imax):
        #         sum = nums[i] + nums[imin] + nums[imax]
        #         if abs(target - sum) < abs(target - closest):
        #             closest = sum
        #
        #         if target > sum:
        #             imin += 1
        #         elif target < sum:
        #             imax -= 1
        #         else:
        #             return target
        #
        #     i += 1
        # return closest

        ## Office Solution, in some cases comparison is not so good for efficiency
        nums.sort()
        i = 0
        closest = -9999999
        while i < len(nums) - 2:
            imin, imax = i + 1, len(nums) - 1
            while (imin < imax):
                sum = nums[i] + nums[imin] + nums[imax]
                if abs(target - sum) < abs(target - closest):
                    closest = sum

                if target > sum:
                    imin += 1
                else:
                    imax -= 1

            i += 1
        return closest


S = [-73, -78, -47, 65, 22, 21, -28, -87, 86, -78, -29, 97, 30, 98, -38, -68, 76, -91, 70, -48, -67, -26, -52, -17, 76, -21, -25, 15, -58, 41, 47, -40, 86, 44, -18, 47, -94, -12, 52, 48, -90, 65, 52, -2, 25, -39, -18, -60, 41, 59, 95, 10, 44, -65, -17, -56, 47, 89, 33, 75, 0, -62, -24, 22, -23, -58, 52, -71, -23, -91, -13, 13, 100, 25, -25, 22, -12, -77, -37, 34, -45, 10, -93, -92, 49, 88, 61, 89, 69, 25, 46, -52, 64, -60, -94, -61, 18, 34, 18, 24, -73, -30, 13, 27, 65, 75, -32, 34, -54, -30, 20, -85, -27, 48, 43, -13, -85, -82, 94, 11, -94, 0, -78, 54, -95, -11, -6, -86, -80, -80, 73, -71, -68, 20, 94, 52, -50, -78, 87, 25, -48, 94, -65, 89, 46, 33, 26, -75, 55, -20, 58, 0, -91, 1, 42, 90, -62, 11, -28, -4, 33, 58, -74, 85, -93, 42, 9, -91, 18, 76]
target = -283
print(Solution().threeSumClosest(S, target))
