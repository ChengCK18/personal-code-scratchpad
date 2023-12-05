class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        preMap = {i:[] for i in range(n)}

        for node1, node2 in (edges): # create a map of node and their corresponding connection.
            preMap[node1].append(node2)
            preMap[node2].append(node1)
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for child in preMap[node]:
                dfs(child)
        
        totalConnectedComponents = 0 
        for ind in range(n):
            if(ind not in visited and len(preMap[ind])>0): # have not visited and it's not a single node without edges
                dfs(ind) # perform dfs on all its corresponding connection and add to visited. Will only end upon all connected explored.
                totalConnectedComponents+=1 # add 1 for a new completed connected components.

        return totalConnectedComponents