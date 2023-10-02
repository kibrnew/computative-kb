# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def lt(root):
            if not root:
                return 
            temp=deque([(root,1)])
            ans=[[]]
            while temp:
                cur=temp.popleft()
                if cur[1]<=len(ans):
                    ans[cur[1]-1].append(cur[0].val)
                else:
                    ans.append([cur[0].val])
                if cur[0].left:
                    temp.append((cur[0].left,cur[1]+1))
                if cur[0].right:
                    temp.append((cur[0].right,cur[1]+1))
            return ans
        ans=lt(root)
        
        if not ans :
            return 0
           
        return sum([len(num) for num in ans ])
