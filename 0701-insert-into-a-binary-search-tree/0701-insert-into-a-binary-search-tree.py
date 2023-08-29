# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bst(root,val):
            if root is None:
                return TreeNode(val)
            if val < root.val:
                root.left = bst(root.left, val)
            else:
                root.right = bst(root.right, val)
            return root
        
        return bst(root,val)
            
            