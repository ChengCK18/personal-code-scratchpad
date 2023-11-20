#Working non-graph based approach :D
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        foundIsland=False
        totalIsland=0
        visited = set()

        def dfs(r,c):
            nonlocal foundIsland
            if(r<0 or
               c<0 or
               r>=ROWS or
               c>=COLS or
               (r,c) in visited):
               return 

            visited.add((r,c))

            if(grid[r][c] == "1"):
                foundIsland = True

            if(grid[r][c] == "0"):
                return 

            grid[r][c]=0 # to mark as visited
           
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return 

        for rw in range(ROWS):
            for cl in range(COLS):
                if((rw,cl) in visited):
                    continue
                dfs(rw,cl)
                if(foundIsland):
                    totalIsland+=1
                foundIsland = False

        return totalIsland


        

                