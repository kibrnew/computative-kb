# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        queue=deque()
        queue.append(root)
        ans=[]
        f=0

        while queue:
            n=len(queue)
            ans.append([])

            for _ in range(n):

                if f:
                    node=queue.pop()
                else:
                    node=queue.popleft()
                if not node:
                    continue

                ans[-1].append(node.val)
                if not f:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.appendleft(node.right)
                    queue.appendleft(node.left)
                    

            f^=1

        ans.pop()

                

        return ans 
                

        
   