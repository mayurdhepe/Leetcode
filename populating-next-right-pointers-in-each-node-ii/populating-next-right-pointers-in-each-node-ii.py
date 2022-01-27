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
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root
        
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            dummy = Node(0)
            
            while (size>0):
                node = queue.popleft()
                dummy.next = node
                dummy = dummy.next
                
                if node.left is not None:
                    queue.append(node.left)
                    
                if node.right is not None:
                    queue.append(node.right)
                    
                size -= 1
                    
        return root
        
        