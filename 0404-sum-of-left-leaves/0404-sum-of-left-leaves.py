# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = [0]
        def traverse(root, side):
            if not root:
                return
            if not root.left and not root.right:
                if side == "l": 
                    s[0]+= root.val
            traverse(root.left,"l")
            traverse(root.right,"r")
        traverse(root,0)
        return s[0]


            
            
    