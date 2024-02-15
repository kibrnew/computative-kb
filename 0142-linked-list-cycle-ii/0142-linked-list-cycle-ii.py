# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        d={}
        temp=head
        i=0
        while temp:
            if temp in d:
                return temp
            d[temp]=1
            temp=temp.next
            i+=1
        return None
        
            
            