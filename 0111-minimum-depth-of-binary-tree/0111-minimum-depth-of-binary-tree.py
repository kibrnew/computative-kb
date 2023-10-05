# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def bfs(node):
            queue=deque()
            queue.append((root,1))
            if not node:
                return 0
            while queue:
                cur,h=queue.popleft()
                left=cur.left
                right=cur.right
                if not (left or right):
                    return h
                if left:
                    queue.append((left,h+1))
                if right:
                    queue.append((right,h+1))
        return bfs(root)
        