# Question No.149 Max Points on a Line
import collections

import math


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtyp
        """
        ## Mine Solution, not so good, but idea is right
        ans = collections.defaultdict(list)

        i, max_num = 0, 0
        while i < len(points):
            max_num = max(max_num, 1)
            j = i + 1
            while j < len(points):
                x1, x2, y1, y2 = points[i].x, points[j].x, points[i].y, points[j].y
                coord = [0] * 3
                if x1 == x2:
                    coord = [1, 0, x1]
                elif y1 == y2:
                    coord = [0, 1, y1]
                else:
                    hcf = self.generateGCD(y2 - y1, x2 - x1)
                    coord[0] = (y2 - y1) / hcf
                    coord[1] = (x2 - x1) / hcf
                    coord[2] = (y1 - x1 * coord[0] / coord[1])
                key = tuple(coord)
                if len(ans[key]) == 0:
                    ans[key] = [0] * len(points)
                ans[key][i], ans[key][j] = 1, 1
                max_num = max(ans[key].count(1), max_num)
                j += 1
            i += 1
        return max_num

    def generateGCD(self, a, b):
        if b == 0:
            return a
        else:
            return self.generateGCD(b, a % b)


s = [[1, 1], [0, 0], [0, 0], [1, 1]]
w = []
for i in s:
    w.append(Point(i[0], i[1]))
print(Solution().maxPoints(w))
