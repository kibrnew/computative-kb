# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        handle=ListNode(0,head)
        start=handle
        count=0
        head=handle
        while head and head.next:
            new=head.next
            while new and new.next and new.val==new.next.val :
                new.next=new.next.next
                count=1     
            if count==1:
                head.next=new.next
                count=0
            else:
                head=head.next
        return start.next
                
                
            
        