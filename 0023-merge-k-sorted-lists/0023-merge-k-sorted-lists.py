# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp=[]
        for node in lists:
            head=node
            while head:
                temp.append(head.val)
                head=head.next
        temp.sort(reverse=True)
        ans=None 
        for i in temp:
            ans=ListNode(i,ans)
        return ans