# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traversal = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preOrder(root)
        return self.traversal
        
    
    def preOrder(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.traversal.append(root.val)
            
            self.preOrder(root.left)
            self.preOrder(root.right)