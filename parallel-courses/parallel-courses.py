from collections import deque
from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        if n == 0:
            return 0
        
        if not relations:
            return 1
        
        graph = defaultdict(list)
        inDegree = {i : 0 for i in range(1, n+1)}
        zeroDegree = deque()
        
        for src, dest in relations:
            graph[src].append(dest)
            inDegree[dest] += 1
        
        for key, val in inDegree.items():
            if val == 0:
                zeroDegree.append(key)
        
        if len(zeroDegree) == 0:
            return -1
        
        totalSemesters = totalCourses = 0

        while zeroDegree:
            size = len(zeroDegree)
            totalSemesters += 1
            
            for _ in range(size):
                totalCourses += 1
                course = zeroDegree.popleft()
            
                for neighbor in graph[course]:
                    inDegree[neighbor] -= 1

                    if inDegree[neighbor] == 0:
                        zeroDegree.append(neighbor)
        
        
        return totalSemesters if totalCourses == n else -1
        