from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        if (n <= 0):
            return res
        if (n==1):
            res.append(0)
            return res
        
        indegree = [0] * n
        adjList = [[] for _ in range(n)]
        for u,v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adjList[u].append(v)
            adjList[v].append(u)
            
        queue = deque()
        for i in range(n):
            if (indegree[i] == 1):
                queue.append(i)
                
        while n>2:
            size = len(queue)
            n -= size
            
            while size>0:
                size -= 1
                v = queue.popleft()
                for neighbor in adjList[v]:
                    indegree[neighbor] -= 1
                    if (indegree[neighbor] == 1):
                        queue.append(neighbor)
                
        
        res = list(queue)
        return res
        
        
        
        
        