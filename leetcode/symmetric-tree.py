# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        stack=[root.left,root.right]
        
        while stack:
            left=stack.pop()
            right=stack.pop()
            if left and right:
                if left.val!=right.val:
                    return False
            elif not(left or right):
                continue 
            else:
                return False 
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True 
                
            
            