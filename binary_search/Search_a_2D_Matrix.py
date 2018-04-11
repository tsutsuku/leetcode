# Question No.29 Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        length, n_col = len(matrix) * len(matrix[0]), len(matrix[0])
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n_col, mid % n_col
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        return False


s = [[1]]
print(Solution().searchMatrix(s, 0))
