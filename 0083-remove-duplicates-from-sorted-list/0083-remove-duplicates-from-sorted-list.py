# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        while head and head.next:
            if head.val==head.next.val:
                temp=head.next.next
                head.next=temp
            else:
                head=head.next
        return start
                
            
        