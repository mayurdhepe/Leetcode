# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr is not None:
            # insert into the right subtree
            if val > curr.val:
                # insert right now
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right
            # insert into the left subtree
            else:
                # insert right now
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left
        return TreeNode(val)
        