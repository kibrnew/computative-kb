# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        oddh = odd
        evenh = even
        oddflag = True
        while head:
            if oddflag:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            oddflag = not oddflag
            head = head.next
        even.next = None
        odd.next = evenh.next
        return oddh.next