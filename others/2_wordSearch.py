class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        visited = set()

        def dfs(r,c,wordIndex):
            
            if (wordIndex == len(word)):# reached the end of word
                return True

            if( r<0 or 
                c<0 or 
                r>= rows or 
                c>= cols or 
                board[r][c]!=word[wordIndex] or
                 (r,c) in visited):
                return False

            #
            visited.add((r,c))

            result = (dfs(r+1, c, wordIndex+1) or 
            dfs(r, c+1, wordIndex+1) or 
            dfs(r-1, c, wordIndex+1) or 
            dfs(r, c-1, wordIndex+1))

            visited.remove((r,c))
            return result

        
        for r in range(rows):
            for c in range(cols):
                result = dfs(r,c,0)
                if (result):
                    return True


        return False