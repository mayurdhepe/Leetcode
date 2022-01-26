# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        
        sumMap = [(root, targetSum - root.val)]
        
        while sumMap:
            node, curr_Sum = sumMap.pop()
            if not node.left and not node.right and curr_Sum == 0:
                return True
            
            if node.right:
                sumMap.append((node.right, curr_Sum - node.right.val))
                
            if node.left:
                sumMap.append((node.left, curr_Sum - node.left.val))
        
        return False