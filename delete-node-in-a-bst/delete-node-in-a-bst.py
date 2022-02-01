# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left and root.right:
                return root.right
            if not root.right and root.left:
                return root.left
            pnt = root.right
            while pnt.left:
                pnt = pnt.left
            root.val = pnt.val
            root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
        