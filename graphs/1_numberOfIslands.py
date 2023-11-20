#:D Working dfs based approach 
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



# bfs-based sol, slower than dfs above
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        totalIsland = 0

        def bfs(r,c):
            que = collections.deque()
            visited.add((r,c))
            que.append((r,c))

            while que:
                rw,cl = que.popleft()

                # check its surrounding top,bot,left,right
                directions = [[0,1],[0,-1],[-1,0],[1,0]]
                for direc in directions:
                    addedRw = rw + direc[0]
                    addedCl = cl + direc[1]
                    if(addedRw in range(ROWS) and addedCl in range(COLS) and 
                    grid[addedRw][addedCl]=="1" and (addedRw,addedCl) not in visited):
                        que.append((addedRw,addedCl))
                        visited.add((addedRw,addedCl))




        for rw in range(ROWS):
            for cl in range(COLS):
                if((rw,cl) not in visited and grid[rw][cl]=="1"):
                    bfs(rw,cl)
                    totalIsland +=1

        return totalIsland

        

                