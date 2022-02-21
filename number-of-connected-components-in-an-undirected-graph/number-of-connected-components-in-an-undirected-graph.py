class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges or len(edges) == 0:
            return n
        
        unionFind = UnionFind(n)
        for A, B in edges:
            unionFind.union(A, B)
            
        return unionFind.getCount()
        
                
class UnionFind:
    def __init__(self,n):
        self.root = [root for root in range(n)]
        self.rank = [1]*n
        self.count = n
        
    
    def find(self, A):
        if A == self.root[A]:
            return A
        
        self.root[A] = self.find(self.root[A])
        return self.root[A]
    
    
    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)
        
        if (rootA != rootB):
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootB] > self.rank[rootA]:
                self.root[rootA] = rootB
            else:
                self.root[rootA] = rootB
                self.rank[rootB] += 1
                
            self.count -= 1
            
    def getCount(self):
        return self.count
            