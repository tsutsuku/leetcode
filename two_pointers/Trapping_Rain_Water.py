# Question No.42 Trapping Rain Water
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ## Mine Solution, works, not elegant
        # total = m = n = 0
        # for i in range(len(height)):
        #     if height[i] > m:
        #         m = height[i]
        #         n = i
        #
        # i = 0
        # while i < n:
        #     while i < n and height[i + 1] >= height[i]:
        #         i += 1
        #     s = i
        #     i += 1
        #     if i >= n:
        #         break
        #     while height[i] < height[s]:
        #         total += height[s] - height[i]
        #         i += 1
        # i = len(height) - 1
        # while i > n:
        #     while i >  n and height[i - 1] >= height[i]:
        #         i -= 1
        #     s = i
        #     i -= 1
        #     if i <= n:
        #         break
        #     while height[i] < height[s]:
        #         total += height[s] - height[i]
        #         i -= 1
        # return total

        # Good Solution
        left, right = 0, len(height) -1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


s = [1, 7,2, 8]
print(Solution().trap(s))
