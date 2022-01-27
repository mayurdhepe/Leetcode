"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root
        
        head = root
        
        while head is not None:
            dummy = Node(0)
            curr = dummy
            
            while head is not None:
                if head.left is not None:
                    curr.next = head.left
                    curr = curr.next
                    
                if head.right is not None:
                    curr.next = head.right
                    curr = curr.next
                    
                head = head.next
                
            head = dummy.next
            
        return root
        