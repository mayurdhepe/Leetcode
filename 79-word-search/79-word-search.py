class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, index):
            if (r<0 or c<0 or r>=rows or c>=cols or index>=len(word) or board[r][c] != word[index] or (r,c) in visited):
                return False
            
            if index == len(word)-1: 
                return True
            
            visited.add((r,c))
            
            c1 = dfs(r+1, c, index+1)
            c2 = dfs(r-1, c, index+1)
            c3 = dfs(r, c+1, index+1)
            c4 = dfs(r, c-1, index+1)
            
            visited.remove((r,c))
            
            return c1 or c2 or c3 or c4
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0):
                    return True
                
        return False