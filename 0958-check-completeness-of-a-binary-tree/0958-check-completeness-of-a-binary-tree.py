# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if not root:
                return
            queue=deque([root])
            ans=[]
            while queue:
                temp=queue.popleft()
                if temp:
                    ans.append(temp.val)
                    if temp.left:
                        queue.append(temp.left)
                    else:
                        queue.append(None)
                    if temp.right:
                        queue.append(temp.right)
                    else:
                        queue.append(None)
                else:
                    ans.append(None)
                
            return ans
        new=traverse(root)
        print(new)
        end=len(new)-1
        for i in range(len(new)):
            ind=len(new)-i-1
            if new[ind]:
                end=ind
                break
        print(new[:end+1])
        return not(None in new[:end+1])
                    
                    
                
                
                
        