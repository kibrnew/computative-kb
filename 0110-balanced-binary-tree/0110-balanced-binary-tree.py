# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, depth):
            if not root:
                return depth
            left=dfs(root.left, depth + 1)
            right=dfs(root.right, depth + 1)
            if not left or not right:
                return False
            if abs(left-right)>1:
                return False
            return max(left,right) 
        if not root:
            return True
        return dfs(root, 0)