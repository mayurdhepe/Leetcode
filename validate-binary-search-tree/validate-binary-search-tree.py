# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidBST(root, None, None)
        
        
    def checkValidBST(self, root: Optional[TreeNode], low: int, high: int) -> bool:
        if root is None: return True
        
        if (low != None and root.val <= low) or (high != None and root.val >= high):
            return False
        
        return self.checkValidBST(root.left, low, root.val) and self.checkValidBST(root.right, root.val, high) 
            
        