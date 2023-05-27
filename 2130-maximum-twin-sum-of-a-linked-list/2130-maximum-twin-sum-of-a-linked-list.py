# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy=ListNode
        dummy.next=head
        fast=head
        slow=dummy
        while fast:
            fast=fast.next
            if fast:
                slow=slow.next
                fast=fast.next
        prev=None
        curr=slow.next
        slow.next=None
        while curr.next:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        curr.next=prev   
        ans=0
        while curr:
            ans=max(curr.val+dummy.next.val,ans)
            curr=curr.next
            dummy=dummy.next
        return ans