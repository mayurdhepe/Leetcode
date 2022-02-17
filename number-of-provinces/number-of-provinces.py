class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i, n):    
                if i != j and isConnected[i][j] == 1:
                    print(uf.root)
                    uf.union(i, j)
        
        distinct_roots = []
        count = 0

        for x in uf.root:
	        root = uf.find(x)
	        if root not in distinct_roots:
		        distinct_roots.append(root)
		        count +=1
		
        print(uf.root)
        print(distinct_roots)
        return count
            
            
                         
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        
    
    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        return x
	
# helper function to create a union between node x and node y
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

