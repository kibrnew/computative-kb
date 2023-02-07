#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        head=ListNode()
        """if head1.val<head2.val:
            head.val=head1.val
            head1=head1.next
        else:
            head.val=head2.val
            head2=head2.next"""
        start=head
        while head1 and head2:
            #newnode=ListNode()
            if head1.val<head2.val:
                cur = head1
                head1=head1.next
                cur.next =None
            else:
                cur = head2
                head2=head2.next
                cur.next = None
            head.next=cur
            head=cur
        if head1:
            head.next=head1
        else:
            head.next=head2
            
        return start.next
        