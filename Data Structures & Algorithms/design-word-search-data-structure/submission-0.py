class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        def dfs (i: int, node: TrieNode) -> bool:

            if i == len(word):
                return node.isEnd
        
            ch = word[i]

            if ch == '.':
                for child in node.children.values():
                    if dfs (i + 1, child):
                        return True
                return False

            if ch not in node.children:
                return False
            
            return(dfs(i + 1, node.children[ch]))
        return dfs(0, self.root)     


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)