class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self,word:str) -> None:
        curr = self.root
        for char in word:
            if(char not in curr.children):
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        curr.isWord = True

    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieStructure = Trie()
        for word in words:
            trieStructure.addWord(word)

        
        resultStrings = set()
        def dfs(r,c,curr,word):
            if(curr.isWord):
                resultStrings.add(word)
                curr.isWord = False
            
            if(r>=ROWS or c>=COLS or 
            r<0 or c<0 or 
            board[r][c] not in curr.children or
            (r,c) in visited):
                return 
            

            
            visited.add((r,c))
            curr = curr.children[board[r][c]]
            word += board[r][c]
           
            dfs(r+1, c, curr,word) 
            dfs(r, c+1, curr,word) 
            dfs(r-1, c, curr,word) 
            dfs(r, c-1, curr,word)
            # print(r,c)

            visited.remove((r,c))
           


        curr = trieStructure.root
        ROWS,COLS = len(board) , len(board[0])
        visited = set()

        for r in range (ROWS):
            for c in range(COLS):
                    result = dfs(r,c,curr,"")
        
        return resultStrings


#Solution: TIME LIMIT EXCEEDED. Need to rely on Trie structure

# '''
# - Trie structure but with links to adjacent node, loop through and keep track of previous node chain
# - Each node marked with unique ID (to keep track of similar node)
# - DFS style traversal
# '''


# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.id = 0



# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         ROWS,COLS = len(board),len(board[0])
#         wordFound = []
#         visited = set()

#         def dfs(r,c,charIndex,wordIndex):
#             if(charIndex == len(words[wordIndex])):
#                 return True
            
#             if(r < 0 or 
#             c < 0 or 
#             r >= ROWS or 
#             c >= COLS or 
#             board[r][c] != words[wordIndex][charIndex] or 
#             (r,c) in visited):
#                 return False
            
#             visited.add((r,c))

#             result= (dfs(r+1,c,charIndex+1,wordIndex) or
#             dfs(r-1,c,charIndex+1,wordIndex) or
#             dfs(r,c+1,charIndex+1,wordIndex) or
#             dfs(r,c-1,charIndex+1,wordIndex)  
#             )

#             visited.remove((r,c))

#             return result

        
#         for wordIndex in range(len(words)):
#             wordFoundBool = False
#             for r in range(ROWS):
#                 if(wordFoundBool):
#                     break
#                 for c in range(COLS):
#                     wordFoundBool = dfs(r,c,0,wordIndex)
#                     if(wordFoundBool):
#                         wordFound.append(words[wordIndex])
#                         break

 
#         return wordFound
            