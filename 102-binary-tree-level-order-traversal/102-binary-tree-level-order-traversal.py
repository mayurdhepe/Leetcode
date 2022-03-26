from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        # 0th level -> root
        queue = deque([[0, root]])
        answer = {}
        
        while queue:
            level, node = queue.popleft()
            if level not in answer:
                answer[level] = []
            
            answer[level].append(node.val)
            
            if node.left:
                queue.append([level+1, node.left])
                
            if node.right:
                queue.append([level+1, node.right])
        
        return [answer[i] for i in range(len(answer))]
        
        
        