# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            print("hey")
            if cur[0].left:
                temp.append((cur[0].left,cur[1]+1))
            if cur[0].right:
                temp.append((cur[0].right,cur[1]+1))
        return ans
                
                
        return ans