# Question No.30 Substring with Concatenation of All Words
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # Mine Solution , not work, Time exceeded
        #     z = []
        #
        #     for i in range(len(s)):
        #         self.findString(s[i:], i, words, z)
        #     return z
        #
        # def findString(self, s, start, map, z):
        #     if len(map) > 1:
        #         hash = set()
        #         for i in map:
        #             n = len(i)
        #             if s[:n] == i and not i in hash:
        #                 hash.add(i)
        #                 temp = map.copy()
        #                 temp.remove(i)
        #                 self.findString(s[n:], start, temp, z)
        #     else:
        #         i = len(map[0])
        #         if s[:i] == map[0]:
        #             z.append(start)

        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        list = []
        n, num, length = len(s), len(words), len(words[0])

        for i in range(n - num * length + 1):
            map = {}
            j = 0
            while j < num:
                word = s[i + j * length:i + (j + 1) * length]
                if word in counts.keys():
                    map[word] = map.get(word, 0) + 1
                    if map[word] > counts.get(word, 0):
                        break
                else:
                    break
                j += 1
            if j == num:
                list.append(i)
        return list


s = "barfoothefoobarman"
words = ["foo", "bar"]
print(Solution().findSubstring(s, words))
