from collections import deque 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = [[] for _ in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        queue = deque([source])
        visited = set([source])
        
        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
            
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return False
                
            
                