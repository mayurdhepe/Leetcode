from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        queue = deque()
        path = [0]
        # we store the entire path in queue
        queue.append(path)
        while queue:
            # pop the oldest path from queue 
            currentPath = queue.popleft()
            # get the last element from path 
            node = currentPath[-1]
            
            # visit all neighbors of that node
            for neighbor in graph[node]:
                tempPath = currentPath.copy()
                tempPath.append(neighbor)
                # if its the last node, then add this path to result       
                if neighbor == len(graph)-1:
                    result.append(tempPath)
                else:
                # add this path to the queue
                    queue.append(tempPath)
                
        return result
        