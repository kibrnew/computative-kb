# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        temp=dummy
        i=0
        while i<n:
            temp=temp.next
            i+=1
        temp2=dummy
        start=temp2
        while temp and temp.next:
            temp=temp.next
            temp2=temp2.next
        if temp2.next:
            temp2.next=temp2.next.next
        else:
            temp2=None
        return start.next
        