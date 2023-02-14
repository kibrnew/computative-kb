# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        count=0
        check=0
        if start and start.next:
            check=start.next.val
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
        count=0
        while start and start.next and start.val==start.next.val:
            start=start.next
            count=1
        if count==1:
            start=start.next
        if start and check==start.val:
            start=start.next
        return start
                
                
            
        