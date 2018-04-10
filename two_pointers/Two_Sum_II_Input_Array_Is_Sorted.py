# Question No.167 Two Sum II - Input array is sorted
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Mine Solution, not elegant
        # i = k = 0
        # while i < len(numbers):
        #     k = i + 1
        #     while k < len(numbers):
        #         if numbers[i] + numbers[k] == target:
        #             return [i + 1, k + 1]
        #         while k + 1 < len(numbers) and numbers[k] == numbers[k + 1]:
        #             k += 1
        #         k += 1
        #     while i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
        #         i += 1
        #     i += 1
        # return None

        # Office Solution, good
        if not numbers or len(numbers) < 2:
            return None
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1
        return None

s = [2,3,4]
print(Solution().twoSum(s, 6))
