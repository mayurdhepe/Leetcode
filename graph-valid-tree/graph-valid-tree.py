class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        unionFind = UnionFind(n)
        for A,B in edges:
            if not unionFind.union(A, B):
                return False
            
        return True
        

class UnionFind:
    def __init__(self,n):
        self.parent = [node for node in range(n)]
        
    
    def find(self, A):
        while self.parent[A] != A:
            A = self.parent[A]
        
        return A
    
    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        
        if root_A == root_B:
            return False
        
        self.parent[root_A] = root_B
        
        return True
    
    
        