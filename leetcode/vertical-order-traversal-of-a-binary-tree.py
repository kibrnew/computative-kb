# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        count=defaultdict(list)
        def dfs(node,h,l):
            if not node:
                return 

            count[h].append((l,node.val))
            dfs(node.left,h-1,l+1)
            dfs(node.right,h+1,l+1)

        dfs(root,0,0)

        keys=sorted(count.keys())
        ans=[]
        for val in keys:
            new=sorted(count[val])
            temp=[]
            for i,val in new:
                temp.append(val)
            ans.append(temp)

        return ans

        