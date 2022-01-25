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
        
        queue = deque([[root, 0]])
        answer = {} 
         
        while len(queue) > 0:
            node, level = queue.popleft()
            if level not in answer:
                answer[level] = []
            answer[level].append(node.val)
            
            if node.left != None:
                queue.append([node.left, level+1])
            
            if node.right != None:
                queue.append([node.right, level+1])
                
        return [answer[l] for l in range(len(answer))]
            
        