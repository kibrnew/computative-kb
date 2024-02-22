class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack=[]
        count=Counter(s)
        visited=set()
        
        for val in s:
            count[val]-=1
            while stack and stack[-1]>=val and count[stack[-1]]>0 and val not in visited:
                v=stack.pop()
                visited.remove(v)
            
            if val not in visited:
                stack.append(val)
                visited.add(val)
            
        return "".join(stack)
        