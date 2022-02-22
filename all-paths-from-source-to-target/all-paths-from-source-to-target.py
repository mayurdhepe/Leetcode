class Solution:
    def __init__(self):
        self.result = []
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph or len(graph) == 0:
            return self.result
        
        self.dfs(graph, 0, [0], self.result)
        return self.result
            
           
    def dfs(self, graph, curr, path, result):
        # destination is the last node i.e. len(n)-1 
        if curr == len(graph)-1:
            result.append(path.copy())
            return
        
        # recurse on neighbors
        for neighbor in graph[curr]:
            path.append(neighbor)
            self.dfs(graph, neighbor, path, result)
            path.pop()
            
            
        
        
        