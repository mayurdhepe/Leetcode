class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.buildGraph(edges)
        visited = [0 for _ in range(n)]
        return self.hasPath(graph, source, destination, visited)
    
    
    def buildGraph(self, edges):
        graph = {}
        for A,B in edges:
            if A not in graph:
                graph[A] = []
            if B not in graph:
                graph[B] = []
            
            graph[A].append(B)
            graph[B].append(A)
        
        return graph
    
    
    def hasPath(self, graph, src, dest, visited):
        if src == dest:
            return True
        
        if visited[src] == 1:
            return False
        
        visited[src] = 1
        for neighbor in graph[src]:
            if self.hasPath(graph, neighbor, dest, visited) == True:
                return True
        
        return False
            
            
                
        