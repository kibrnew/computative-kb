# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        print(l)
        stack=[]
        for i in l:
            if not (stack) or stack[-1]>=i:
                stack.append(i)
            else:
                while stack and stack[-1]<i:
                    stack.pop()
                stack.append(i)
        new=head
        for i in range(len(stack)):
            head.val=stack[i]
            if i==len(stack)-1:
                head.next=None
            else:
                head=head.next
        return new
        
        
        
            