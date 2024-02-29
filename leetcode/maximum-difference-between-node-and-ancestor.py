# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node,maxi,mini):
            if not node:
                return maxi-mini

            maxi=max(node.val,maxi)
            mini=min(node.val,mini)

            return max(dfs(node.left,maxi,mini),dfs(node.right,maxi,mini))

        return dfs(root,root.val,root.val)
        