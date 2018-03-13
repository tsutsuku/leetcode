class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        all = len(nums2) + len(nums1)
        mid = (int)((len(nums1) + len(nums2)) / 2)
        if (len(nums2) > 0):
            for i in range(len(nums1)):
                insertMid = self.quickInsert(nums2, nums1[i])
                nums2.insert(insertMid, nums1[i])

                if (insertMid + 1 > mid):
                    break
        else:
            nums2 = nums1

        if all % 2 == 0:
            return (nums2[mid] + nums2[mid - 1]) / 2.0
        else:
            return nums2[mid]

    def quickInsert(self, nums, num):
        start = 0
        last = len(nums)

        while (1):
            mid = (int)((start + last) / 2.0)
            if nums[mid] < num:
                start = mid
            elif nums[mid] > num:
                last = mid
            else:
                return mid

            if (last == start + 1 or last == start):
                if num > nums[start]:
                    return last
                else:
                    return start

    ##Good Solution
    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                return (max_of_left + min_of_right) / 2.0


nums1 = [1, 2, 3]
nums2 = [1, 2]
# print(Solution().insertNum(nums2, 5.5))
print(Solution().findMedianSortedArrays(nums1, nums2))
