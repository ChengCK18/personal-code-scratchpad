"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(node is None):
            return None

        visited = {}
        finalGraph = Node(node.val)
        visited[node.val] = finalGraph

        def bfs(node):
            que = collections.deque([node])

            while que:
                node = que.popleft()
                for ngh in node.neighbors:
                    if(ngh.val not in visited):
                        visited[ngh.val] = Node(ngh.val)
                        que.append(ngh)
    
                    visited[node.val].neighbors.append(visited[ngh.val])
        
                
         
        bfs(node)
        return finalGraph
        