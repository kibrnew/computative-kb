# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        if not head.next:
            return head
        while fast:
            fast=fast.next
            if fast:
                slow=slow.next
                fast=fast.next
        return slow
    