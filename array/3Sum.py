##Question No.15 3Sum

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Not good Solution
        # nums.sort()
        # list = []
        # header = []
        # key = False
        # i = 0
        # while i <= len(nums) -3:
        #     if header.count(nums[i]) == 0:
        #         imin, imax = i + 1, len(nums) - 1
        #         header.append(nums[i])
        #         key = False
        #         while (imin < imax):
        #             sum = nums[i] + nums[imin] + nums[imax]
        #
        #             if sum == 0 and not key:
        #                 list.append([nums[i], nums[imin], nums[imax]])
        #                 key = True
        #             if sum != 0:
        #                 key = False
        #
        #             if sum >= 0:
        #                 imax -= 1
        #             else:
        #                 imin += 1
        #     i += 1
        # return list

        # Good Solution
        nums.sort()
        list = []
        i = 0
        while i < len(nums) - 2:
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                imin, imax = i + 1, len(nums) - 1
                while (imin < imax):
                    sum = nums[i] + nums[imin] + nums[imax]
                    if sum == 0:
                        list.append([nums[i], nums[imin], nums[imax]])
                        while (imin < imax and nums[imin + 1] == nums[imin]):
                            imin += 1
                        while (imin < imax and nums[imax - 1] == nums[imax]):
                            imax -= 1
                        imin+= 1
                        imax-= 1
                    elif sum > 0:
                        imax -= 1
                    else:
                        imin += 1

            i += 1
            if nums[i] > 0:
                break
        return list


S = [-1,0,1,2,-1,-4]
print(Solution().threeSum(S))
