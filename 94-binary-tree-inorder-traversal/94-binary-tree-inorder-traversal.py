# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return self.ans
        
        self.inorder(root)
        return self.ans
    
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            
            self.ans.append(root.val)
            
            self.inorder(root.right)
        