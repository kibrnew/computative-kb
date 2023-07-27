# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(node,s):
            if not node:
                return False 
            s+=node.val
            if not(node.left or node.right):
                if s==targetSum:
                    return True
            left=traverse(node.left,s)
            right=traverse(node.right,s)
            if left or right:
                return True
            return False
        return traverse(root,0)