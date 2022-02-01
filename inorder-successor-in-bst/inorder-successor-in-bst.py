# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    previous = None
    inorder_successor = None
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        self.previous, self.inorder_successor = None, None
        
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
                
            self.inorder_successor = leftmost
        else:
            self.inorderCase2(root, p)
            
        return self.inorder_successor
    
    
    def inorderCase2(self, node: 'TreeNode', p: 'TreeNode'):
        if not node: return
        
        # recurse on the left side
        self.inorderCase2(node.left, p)
        
        # Check if previous is the inorder predecessor of node
        if self.previous == p and not self.inorder_successor:
            self.inorder_successor = node
            return
        
        # Keeping previous up-to-date for further recursions
        self.previous = node
        
        # recurse on the right side
        self.inorderCase2(node.right, p)
    
    
    
    
    
    
    
    
        