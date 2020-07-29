#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):
    # 借助迭代实现前缀树的查询与插入
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root

        # 在Trie查找并插入每个字符
        for c in word:
            if c in node:
                node = node[c]
            else:
                node[c] = {}
                node = node[c]

        node["$"] = "$"     # 表示单词的结束            


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root

        for c in word:
            if c in node:
                node = node[c]
            else:
                return False

        if "$" in node:
            return True
        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root

        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

