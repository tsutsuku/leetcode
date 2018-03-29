#Question No.208 Implement Trie(Prefix Tree)
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.links = [Trie()] * 26


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """