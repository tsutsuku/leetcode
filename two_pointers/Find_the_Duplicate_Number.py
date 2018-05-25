#Question No.287 Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##Not find a Solution
        ##Office Solution 1 Sorting, not good
        ## Time complexity: O(nlgn), Space complexity: O(n)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return nums[i]

        ##Office Solution 2 Set, not good
        ##Time complexity: O(n), Space complexity: O(n)
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        ##Office Solution 3 Floyd's Tortoise and Hare(Cycle Detection)
        ##Time complexity: O(n), Space complexity: O(1)
        t = nums[0]
        h = nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break

        p1 = nums[0]
        p2 = t
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1