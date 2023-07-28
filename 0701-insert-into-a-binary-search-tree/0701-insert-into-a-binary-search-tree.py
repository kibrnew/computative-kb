# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def traverse(root):
            if not root:
                return 
            flag=0
            if not(root.left): 
                if root.val>val:
                    root.left=TreeNode(val)
                    flag=-1
            if not(root.right):
                if root.val<val:
                    root.right=TreeNode(val)
                    flag=-1
            if flag==0:
                if root.val>val:
                    traverse(root.left)
                elif root.val<val:
                    traverse(root.right)
        traverse(root)
        return root
            
            