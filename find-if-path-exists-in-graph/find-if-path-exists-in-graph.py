class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = self.buildGraph(n, edges)
        
        stack = [source]
        visited = set()
        
        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            if node in visited:
                continue
            
            visited.add(node)
            for neighbor in adjlist[node]:
                stack.append(neighbor)
        
        return False
            
    
    def buildGraph(self, n, edges):
        adjlist = [[] for i in range(n)]
        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
            
        return adjlist
        
        