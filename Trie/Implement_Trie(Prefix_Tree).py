# Question No.208 Implement Trie(Prefix Tree)
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if not node.contiansKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node != None and node.isEnd()

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.searchPrefix(prefix)
        return node != None

    def searchPrefix(self, word):
        node = self.root
        for ch in word:
            if node.contiansKey(ch):
                node = node.get(ch)
            else:
                return None
        return node

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.R = 26
        self.is_end = False

    def contiansKey(self, ch):
        return self.links[ord(ch) - ord('a')] != None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.is_end = True

    def isEnd(self):
        return self.is_end

obj = Trie()
obj.insert('app')
print(obj.search('apps'))
print(obj.search('app'))
