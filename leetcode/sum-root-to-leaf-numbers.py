# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return []

            left=dfs(node.left)
            right=dfs(node.right)
            ans=[]
            for val in (left+right):
                ans.append(str(node.val)+val)
            if not ans:
                ans.append(str(node.val))
            return ans 

        res=dfs(root)
        ans=0
        for val in res:
            ans+=int(val)
        return ans 

        

            
        