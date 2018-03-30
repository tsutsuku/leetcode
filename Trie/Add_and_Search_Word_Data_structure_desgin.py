# Question No.211 Add and Search Word Data structure design
# Mine Solution, not so good
# class WordDictionary:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()
#
#     def addWord(self, word):
#         """
#         Adds a word into the data structure.
#         :type word: str
#         :rtype: void
#         """
#         node = self.root
#         for ch in word:
#             if not node.contiansKey(ch):
#                 node.put(ch, TrieNode())
#             node = node.get(ch)
#
#         node.setEnd()
#
#     def search(self, word):
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         :type word: str
#         :rtype: bool
#         """
#         node = self.searchPrefix(word, self.root)
#         return node != None and node.isEnd()
#
#     def searchPrefix(self, word, root):
#         node = root
#         for i in range(len(word)):
#             if word[i] == '.':
#                 for j in list(filter(lambda x: x != None, node.links)):
#                     t = self.searchPrefix(word[i+1:], j)
#                     if t != None and t.isEnd():
#                         return t
#                 else:
#                     return None
#             elif node.contiansKey(word[i]):
#                 node = node.get(word[i])
#             else:
#                 return None
#         return node
#
#
# class TrieNode:
#     def __init__(self):
#         self.links = [None] * 26
#         self.R = 26
#         self.is_end = False
#
#     def contiansKey(self, ch):
#             return self.links[ord(ch) - ord('a')] != None
#
#     def get(self, ch):
#             return self.links[ord(ch) - ord('a')]
#
#     def put(self, ch, node):
#             self.links[ord(ch) - ord('a')] = node
#
#     def setEnd(self):
#         self.is_end = True
#
#     def isEnd(self):
#         return self.is_end

# Office Solution
import collections


class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False

obj = WordDictionary()
obj.addWord('a')
print(obj.search('.a'))
print(obj.search('ap.'))
print(obj.search('ok'))
