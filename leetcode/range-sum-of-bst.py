# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans=[]
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        res=0
        for val in ans:
            if low<=val<=high:
                res+=val
        return res
        