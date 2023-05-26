# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        if not head:
            return False
        while fast.next:
            fast=fast.next
            if fast==slow:
                return True
            if fast.next:
                fast=fast.next
                if fast==slow:
                    return True
                slow=slow.next
        return False