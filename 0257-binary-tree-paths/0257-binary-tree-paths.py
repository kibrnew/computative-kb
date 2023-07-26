# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def path_maker(l):
            new=[]
            for i in l:
                new.append(str(i))
            return "->".join(new)
        ans=[]  
        def traverse(node,path):
            if not node:
                return 
            path.append(node.val)
            if not(node.left or node.right):
                ans.append(path_maker(path))
            else:
                traverse(node.left,path)
                traverse(node.right,path)
            path.pop()
        traverse(root,[])
        return ans
            