class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if(c not in curr.children):
                curr.children[c] = Node()

            curr = curr.children[c]
        curr.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(word,child):
            curr = child
            for i in range(len(word)):
                c = word[i]
                if(c == '.'):
                    for child in curr.children.values():
                        if(dfs(word[i+1:],child)):
                            return True
                    return False
                else:
                    if(c not in curr.children):
                        return False
                    curr = curr.children[c]

            return curr.isWord

        return dfs(word,self.root)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)