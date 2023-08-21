# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=[0]
        def traverse(node,m):
            if not node :
                return 
            if node.val>=m:
                print(node.val,m)
                count[0]+=1
            left=traverse(node.left,max(node.val,m))
            right=traverse(node.right,max(node.val,m))
        traverse(root,-float("inf"))
        return count[0]