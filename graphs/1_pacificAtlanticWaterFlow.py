#TLE, 111/113. Need optimization
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # to be true
        # pacific =  0 in (x and/or y)
        # atlantic = len(m)-1 or len(n)-1 in (x and/or y)
        ROWS, COLS = len(heights),len(heights[0])
        finalResult = []

        def bfsFlowFromOrigin(rw,cl):
            visited = set()
            reachPacific,reachAtlantic = False, False
            que = collections.deque()
            que.append((rw,cl))

            while que:
                row,col = que.popleft()
                visited.add((row,col))
                if(row == 0 or col == 0):
                    reachPacific = True
                if(row == ROWS-1 or col == COLS-1):
                    reachAtlantic = True

                if(reachPacific and reachAtlantic): # no point continuing, both cond fulfilled
                    return True 
        
                currNodeVal = heights[row][col]
                direction = [[1,0],[-1,0],[0,1],[0,-1]] # north, south, east, west

                for direc in direction:
                    addedRw = row+direc[0] 
                    if addedRw>=ROWS:
                        continue
                    addedCol = col+direc[1]
                    if addedCol>=COLS:
                        continue

                    if(heights[addedRw][addedCol]<=currNodeVal and 
                        (addedRw,addedCol) not in visited):

                        que.append((addedRw,addedCol))
                    

            return reachPacific and reachAtlantic


        for rw in range(ROWS):
            for cl in range(COLS):
                result = bfsFlowFromOrigin(rw,cl)
                if(result):
                    finalResult.append([rw,cl])

       
        return finalResult

