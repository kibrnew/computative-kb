# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        nums.sort()
        head=start
        for i in nums:
            start.val=i
            start=start.next
        return head
        