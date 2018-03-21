# Question No.18 4Sum
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        list = []
        n = len(nums)

        i = 0
        nums.sort()
        while i < n - 3 :
            if i == 0 or (i > 0 and nums[i] != nums[i -1]):
                j = i + 1
                while j < n - 2:
                    if j == i+ 1 or (j > i + 1 and nums[j] != nums[j - 1]):
                        min, max = j + 1, n - 1
                        while min < max:
                            sum = nums[i] + nums[j] + nums[min] + nums[max]
                            if sum == target:
                                list.append([nums[i], nums[j], nums[min], nums[max]])
                                while (min < max and nums[min + 1] == nums[min]):
                                    min += 1
                                while (min < max and nums[max - 1] == nums[max]):
                                    max -= 1
                                min += 1
                                max -= 1
                            elif sum < target:
                                min += 1
                            else:
                                max -= 1
                    j += 1
            i += 1
        return list


s =  [1, 0, -1, 0, -2, 2]
print(Solution().fourSum(s, 0))
