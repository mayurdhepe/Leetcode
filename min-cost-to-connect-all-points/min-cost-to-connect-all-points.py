import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        
        size = len(points)
        priorityQueue = []
        visited = [False] * size
        
        # Add all edges from points[0] vertexs
        x1, y1 = points[0]
        for j in range(1, size):
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, j, cost)
            priorityQueue.append(edge)
        
        # heapify -- form min heap
        heapq.heapify(priorityQueue)
        
        result = 0
        count = size - 1  # MST has n-1 edges
        visited[0] = True
        
        while priorityQueue and count > 0:
            edge = heapq.heappop(priorityQueue)
            point1 = edge.point1
            point2 = edge.point2
            weight = edge.weight
            
            # if the point2 is not visited, then visit it
            if not visited[point2]:
                result += weight
                visited[point2] = True
                # add all its outgoing edges (to non-visited vertices) into the heap
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                        abs(points[point2][1] - points[j][1])
                        edge = Edge(point2, j , distance)
                        heapq.heappush(priorityQueue, edge)
                count -= 1
                
        return result
    
    
class Edge:
    def __init__(self, p1, p2, w):
        self.point1 = p1
        self.point2 = p2
        self.weight = w
    
    def __lt__(self, other):
        return self.weight < other.weight
            