class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for A,B in pairs:
            uf.union(A, B)
            
        # get all connected components    
        groups = {}
        for i in range(n):
            parent = uf.find(i)
            if parent not in groups:
                groups[parent] = []
                
            groups[parent].append(i)
            
        print(groups)
        # sort each connected component
        ans = ["a" for _ in range(n)]
        for group in groups.values():
            temp = [s[i] for i in group]
            temp.sort()
            
            for j in range(len(group)):
                ans[group[j]] = temp[j]
                
    
        return "".join(ans)
        
            

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