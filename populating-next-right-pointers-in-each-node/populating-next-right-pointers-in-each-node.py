"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        
        prevLevel = 0
        prevNode = None
        queue = deque()
        queue.append((1,root))
        
        while queue:
            level, node = queue.popleft()
            
            if level == prevLevel:
                prevNode.next = node
                prevNode = node
            else:
                prevLevel = level
                prevNode = node
                
            if node.left:
                queue.append((level+1, node.left))
                queue.append((level+1, node.right))
        
        return root
            
            
            
            
            
            
        