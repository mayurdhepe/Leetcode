# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        answer = []
        
        if root:
            stack.append(root)
            
        while len(stack) > 0:
            curr = stack.pop()
            answer.append(curr.val)
            
            if curr.right:
                stack.append(curr.right)
                
            if curr.left:
                stack.append(curr.left)
 
        return answer
        