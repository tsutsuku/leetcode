##Question No.11 Contianer With Most Water

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        imin, imax = 0, len(height) - 1
        hmin, hmax = height[imin], height[imax]
        max_water = (imax - imin) * min(height[imin], height[imax])
        while(imin < imax):
            while(height[imin] <= hmin):
                imin = imin + 1
                if (imin >= imax):
                    break
            hmin = height[imin]

            if (imin < imax):
                water = (imax - imin) * min(hmax, hmin)
                if (water < max_water):
                    max_water = water

            while(height[imax] <= hmax):
                imax = imax - 1
                if (imin >= imax):
                    break
            hmax = height[imax]

            if (imin < imax):
                water = (imax - imin) * min(hmax, hmin)
                if (water < max_water):
                    max_water = water
        return max_water

height = [1, 2, 4, 3]
print(Solution().maxArea(height))