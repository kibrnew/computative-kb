# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:    
        flag=[None]
        def traverse(node):
            if node is None:
                return 
            if node.left is not None:
                node.left.parent=node
            if node.right is not None:
                node.right.parent=node
            traverse(node.left)
            traverse(node.right)
            if node.val==start:
                flag[0]=node
        root.parent=None
        traverse(root)       
        queue=deque()
        queue.append((flag[0],0))
        duration={}
        duration[flag[0]]=0
        while queue:
            node,time=queue.popleft()
            for temp in [node.left,node.right,node.parent]:
                if temp and temp not in duration:
                    duration[temp]=time+1
                    queue.append((temp,time+1))
        return max(duration.values())
                
            
        

        

        
        
        
        
        
        
        
        
        
        