# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        total_count, is_unival = self.helper(root)
        return total_count
    
    def helper(self, root):
        if not root: return (0, True)
        
        left_count, is_left_unival = self.helper(root.left)
        right_count, is_right_unival = self.helper(root.right)
        is_unival = True
        
        if not is_left_unival or not is_right_unival:
            is_unival = False
            
        if root.left is not None and root.val != root.left.val:
            is_unival = False
            
        if  root.right is not None and root.val != root.right.val:
            is_unival = False
        
        if is_unival:
            return (left_count+right_count+1, True)
        else: 
            return (left_count+right_count, False)
    
        