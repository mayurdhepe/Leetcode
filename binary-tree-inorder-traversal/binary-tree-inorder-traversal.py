# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traversal = []
        
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inOrder(root)
        return self.traversal
        
        
    def inOrder(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inOrder(root.left)
            self.traversal.append(root.val)
            self.inOrder(root.right)
        