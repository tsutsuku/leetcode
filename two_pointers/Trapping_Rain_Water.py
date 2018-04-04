#Question No.42 Trapping Rain Water
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        k = 0
        if k < 3:
            return 0

        c = total = 0

        while k < len(height):
            k += 1
            if height[k] > height[k - 1]:
                j = i = k
                while i >0:
                    i -= 1
                    if height[i + 1] > height[i]:

                        break
                    i -= 1
                while j < len(height):

        while j < len(height):
            j += 1



            while height[j] < height[i]:
                c += height[i] - height[j]
                j += 1
                if j == len(height):
                    return total
            total, c, i = total + c, 0, j
        return total

s = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(s))