# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False  
        return self.recPathSum(root, targetSum, 0)
        
           
    def recPathSum(self, root: Optional[TreeNode], targetSum: int, currSum: int) -> bool:
        if root is None: return False
        
        currSum += root.val
            
        if not root.left and not root.right:
            if currSum == targetSum:
                return True
         
        return self.recPathSum(root.left, targetSum, currSum) or self.recPathSum(root.right, targetSum, currSum)
            
        
        
        
        
            
        
        
        