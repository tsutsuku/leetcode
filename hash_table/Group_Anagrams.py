# Question No.49 Group Anagrams
import collections


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    # Mine Solution, not work. Time limit exceeded
    #     dic = {}  ## len(word), map:{} ##word, list index
    #     words = []
    #     for word in strs:
    #         if len(word) in dic:
    #             map = dic[len(word)]
    #             for key in map.keys():
    #                 if self.contian(word, key):
    #                     words[map[key]].append(word)
    #                     break
    #             else:
    #                 map[word] = len(words)
    #                 word_list = [word]
    #                 words.append(word_list)
    #         else:
    #             word_list = [word]
    #             dic[len(word)] = {word: len(words)}
    #             words.append(word_list)
    #     return words
    #
    # def contian(self, str, word):
    #     i = 0
    #     if len(str) == len(word):
    #         while i < len(word) and str.count(word[i]) == word.count(word[i]):
    #             i += 1
    #         if i == len(word):
    #             return True
    #     return False

    # Office Solution
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
