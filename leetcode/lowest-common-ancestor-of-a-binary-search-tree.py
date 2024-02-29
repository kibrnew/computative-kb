# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):

            maxi=max(p.val,q.val)
            mini=min(q.val,p.val)

            if mini<=node.val<=maxi:
                return node

            if node.val<mini:
                return dfs(node.right)
            if node.val>maxi:
                return dfs(node.left)
                
        return dfs(root)
        