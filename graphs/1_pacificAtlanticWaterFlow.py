
# solution --- inverse the problem and start from the edges bordering the ocean, to avoid naive try all approach
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # to be true
        # pacific =  0 in (x and/or y)
        # atlantic = len(m)-1 or len(n)-1 in (x and/or y)


        ROWS, COLS = len(heights), len(heights[0]) 
        visitedPacific, visitedAtlantic = set() , set()
        finalResult = []


        def dfs(row,col,visited,prevHeight):
            if((row,col) in visited or
            row not in range(ROWS) or
            col not in range(COLS) or 
            heights[row][col]<prevHeight): # going uphill instead of downhill
                return

            visited.add((row,col))

            directions = [[1,0],[-1,0],[0,1],[0,-1]] # north, south, east, west

            for direc in directions: 
                dfs(row+direc[0],col+direc[1],visited,heights[row][col])




        for cl in range(COLS):
            dfs(0,cl,visitedPacific,heights[0][cl])
            dfs(ROWS-1,cl,visitedAtlantic, heights[ROWS-1][cl])

        for rw in range(ROWS):
            dfs(rw,0,visitedPacific,heights[rw][0])
            dfs(rw,COLS-1,visitedAtlantic,heights[rw][COLS-1])

        for rw in range(ROWS):
            for cl in range(COLS):
                if ((rw,cl) in visitedPacific and (rw,cl) in visitedAtlantic):
                    finalResult.append([rw,cl])
            
        return finalResult





#still TLE, 111/113. Need further optimization or diff algo
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         # to be true
#         # pacific =  0 in (x and/or y)
#         # atlantic = len(m)-1 or len(n)-1 in (x and/or y)
#         ROWS, COLS = len(heights),len(heights[0])
#         finalResult = []
#         main_visited = {}
#         def bfsFlowFromOrigin(rw,cl):
#             visited = set()
#             reachPacific,reachAtlantic = False, False
#             que = collections.deque()
#             que.append((rw,cl))

#             while que:
#                 row,col = que.popleft()
#                 visited.add((row,col))
#                 if(row == 0 or col == 0):
#                     reachPacific = True
#                 if(row == ROWS-1 or col == COLS-1):
#                     reachAtlantic = True

#                 if(reachPacific and reachAtlantic): # no point continuing, both cond fulfilled
#                     return True 
        
#                 currNodeVal = heights[row][col]
#                 direction = [[1,0],[-1,0],[0,1],[0,-1]] # north, south, east, west

#                 for direc in direction:
#                     addedRw = row+direc[0]
#                     addedCol = col+direc[1]

#                     if((addedRw,addedCol) in main_visited and # dont have to visit the same node again 
#                     heights[addedRw][addedCol]<=currNodeVal
#                     ):
#                         reachPacific = main_visited[(addedRw,addedCol)][0] or reachPacific
#                         reachAtlantic = main_visited[(addedRw,addedCol)][1] or reachAtlantic
#                         continue
#                     if(
#                         addedRw in range(ROWS) and
#                         addedCol in range(COLS) and 
#                         heights[addedRw][addedCol]<=currNodeVal and 
#                         (addedRw,addedCol) not in visited  
#                         ):

#                         que.append((addedRw,addedCol))


#             main_visited[(rw,cl)] = (reachPacific,reachAtlantic)
#             return reachPacific and reachAtlantic


#         for rw in range(ROWS):
#             for cl in range(COLS):
#                 result = bfsFlowFromOrigin(rw,cl)
#                 if(result):
#                     finalResult.append([rw,cl])

       
#         return finalResult





#TLE, 111/113. Need optimization
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         # to be true
#         # pacific =  0 in (x and/or y)
#         # atlantic = len(m)-1 or len(n)-1 in (x and/or y)
#         ROWS, COLS = len(heights),len(heights[0])
#         finalResult = []

#         def bfsFlowFromOrigin(rw,cl):
#             visited = set()
#             reachPacific,reachAtlantic = False, False
#             que = collections.deque()
#             que.append((rw,cl))

#             while que:
#                 row,col = que.popleft()
#                 visited.add((row,col))
#                 if(row == 0 or col == 0):
#                     reachPacific = True
#                 if(row == ROWS-1 or col == COLS-1):
#                     reachAtlantic = True

#                 if(reachPacific and reachAtlantic): # no point continuing, both cond fulfilled
#                     return True 
        
#                 currNodeVal = heights[row][col]
#                 direction = [[1,0],[-1,0],[0,1],[0,-1]] # north, south, east, west

#                 for direc in direction:
#                     addedRw = row+direc[0] 
#                     if addedRw>=ROWS:
#                         continue
#                     addedCol = col+direc[1]
#                     if addedCol>=COLS:
#                         continue

#                     if(heights[addedRw][addedCol]<=currNodeVal and 
#                         (addedRw,addedCol) not in visited):

#                         que.append((addedRw,addedCol))
                    

#             return reachPacific and reachAtlantic


#         for rw in range(ROWS):
#             for cl in range(COLS):
#                 result = bfsFlowFromOrigin(rw,cl)
#                 if(result):
#                     finalResult.append([rw,cl])

       
#         return finalResult

