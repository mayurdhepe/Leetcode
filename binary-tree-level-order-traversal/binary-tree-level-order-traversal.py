# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque([[0, root]])
        answer = {} 
         
        while len(queue) > 0:
            level, node = queue.popleft()
            if level not in answer:
                answer[level] = []
            answer[level].append(node.val)
            
            if node.left != None:
                queue.append([level+1, node.left])
            
            if node.right != None:
                queue.append([level+1, node.right])
                
        return [answer[l] for l in range(len(answer))]
            
        