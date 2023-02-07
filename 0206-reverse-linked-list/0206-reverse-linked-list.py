# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        temp=None 
        while current:
            nex=current.next
            current.next=temp
            temp=current
            current=nex
            
        return temp
            
        