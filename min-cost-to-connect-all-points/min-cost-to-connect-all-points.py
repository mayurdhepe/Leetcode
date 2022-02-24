import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        
        size = len(points)
        priorityQueue = []
        uf = UnionFind(size)
        
        for i in range(size):
            x1, y1 = points[i]
            for j in range(i+1, size):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                priorityQueue.append(edge)
                
        heapq.heapify(priorityQueue)
        
        result = 0
        count = size - 1  # MST has n-1 edges
        while priorityQueue and count > 0:
            edge = heapq.heappop(priorityQueue)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                result += edge.weight
                count -= 1
                
        return result
    
    
class Edge:
    def __init__(self, p1, p2, w):
        self.point1 = p1
        self.point2 = p2
        self.weight = w
    
    def __lt__(self, other):
        return self.weight < other.weight
        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
                                
        