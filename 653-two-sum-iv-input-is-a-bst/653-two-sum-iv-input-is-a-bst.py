# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.doesTargetExist(root, k, set())
        
    
    def doesTargetExist(self, root, target, values):
        if root is None:
            return False
        
        if (target - root.val) in values:
            return True
        else:
            values.add(root.val)
            
        isLeft = self.doesTargetExist(root.left, target, values)
        isRight = self.doesTargetExist(root.right, target, values)
        
        return isLeft or isRight
        