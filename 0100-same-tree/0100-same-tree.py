# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorder(root,l):
            if not root:
                l.append(None)
                return l 
            l.append(root.val)
            l=preorder(root.left,l)
            l=preorder(root.right,l)
            return l
        def inorder(root,l):
            if not root:
                l.append(None)
                return l 
            l=inorder(root.left,l)
            l.append(root.val)
            l=inorder(root.right,l)
            return l
        # def postorder(root,l):
        #     if not root:
        #         l.append(None)
        #         return l
        #     l=postorder(root.left,l)
        #     l=postorder(root.right,l)
        #     l.append(root.val)
        #     return l
        return preorder(p,[])==preorder(q,[]) and inorder(p,[])==inorder(q,[])