# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        node=head
        while node:
            ans.append(node.val)
            node=node.next
        ans.sort()
        new=head
        i=0
        while head:
            head.val=ans[i]
            head=head.next
            i+=1
        return  new
        