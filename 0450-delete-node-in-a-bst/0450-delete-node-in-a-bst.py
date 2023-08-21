# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minvalue(bstnode):
            current = bstnode
            while (current.left is not None):
                current = current.left 
            return current
        def traverse(root):
            if not root:
                return root
            if key<root.val:
                root.left=traverse(root.left)
            elif key>root.val:
                root.right=traverse(root.right)
            else:
                if root.left is None :
                    temp=root.right
                    root=None
                    return temp
                if root.right is None :
                    temp=root.left
                    root=None 
                    return temp
                temp=minvalue(root.right)
                root.val=temp.val
                temp.val=key
                root.right=traverse(root.right)
            return root
        return traverse(root)            
                
                