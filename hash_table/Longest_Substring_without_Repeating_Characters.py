# Question No.3 Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Mine Solution
        # if len(s) == 0:
        #     return 0
        #
        # lo, hi = 0, 1
        # min, max = 0, 0
        # map = {}
        # for i in range(len(s)):
        #     hi = i
        #     if s[i] in map:
        #         if lo <= map[s[i]]:
        #             lo = map[s[i]] + 1
        #     if hi - lo > max - min:
        #         max, min = hi, lo
        #     map[s[i]] = i
        #
        # return max - min + 1

        # Sliding Window
        # n = len(s)
        # s_set = set()
        # ans, i, j = 0, 0, 0
        # while i < n and j < n:
        #     if not s[j] in s_set:
        #         s_set.add(s[j])
        #         j += 1
        #         ans = max(ans, j - i)
        #     else:
        #         s_set.remove(s[i])
        #         i += 1
        # return ans

        # Sliding Window Optimized
        n = len(s)
        ans, i, j = 0, 0, 0
        map = {}
        while j < n:
            if s[j] in map:
                i = max(i, map[s[j]])
            ans = max(ans, j - i + 1)
            map[s[j]] = j + 1
            j += 1
        return ans


s = "auuuuk"
print(Solution().lengthOfLongestSubstring(s))
