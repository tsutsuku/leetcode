##Question No.11 Contianer With Most Water

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """



        ##Good Solution
        imin, imax = 0, len(height) - 1
        max_area = 0
        while (imin < imax):
            max_area = max(max_area, (imax - imin) * min(height[imax], height[imin]))
            if (height[imax] > height[imin]):
                imin += 1
            else:
                imax -= 1
        return max_area

        ## Office Recommand Solution
        # imin, imax = 0, len(height) - 1
        # max_area = 0
        # while (imin < imax):
        #     max_area = max(max_area, (imax - imin) * min(height[imax], height[imin]))
        #     if (height[imax] > height[imin]):
        #         imin += 1
        #     else:
        #         imax -= 1
        # return max_area

        ## Bad Mass
        # max_water = (imax - imin) * min(height[imin], height[imax])
        # while (imin < imax):
        #     if reverse:
        #         if height[imin + 1] <= height[imax]:
        #             imin = imin + 1
        #             if height[imin] > height[imin - 1]:
        #                 water = (imax - imin) * min(height[imin], height[imax])
        #                 if (max_water < water):
        #                     max_water = water
        #             continue
        #         else:
        #             reverse = not reverse
        #     else:
        #         if height[imax - 1] <= height[imin]:
        #             imax = imax - 1
        #             if height[imax] > height[imax + 1]:
        #                 water = (imax - imin) * min(height[imin], height[imax])
        #                 if (max_water < water):
        #                     max_water = water
        #             continue
        #         else:
        #             reverse = not reverse
        # return max_water


height = [2, 3, 10, 5, 7, 8, 9]
print(Solution().maxArea(height))
