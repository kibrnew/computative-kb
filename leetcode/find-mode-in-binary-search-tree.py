# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        count=Counter()

        def dfs(node):
            if not node:
                return 

            count[node.val]+=1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        maxi=max(count.values())
        ans=[]
        for key,val in count.items():
            if val==maxi:
                ans.append(key)

        return ans

        