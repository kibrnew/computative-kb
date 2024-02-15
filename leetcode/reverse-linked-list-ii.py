# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        ans=[]
        temp=head
        while temp:
            ans.append(temp.val)
            temp=temp.next
        
        ans[left-1:right]=ans[left-1:right][::-1]
        temp=head
        i=0
        while head:
            head.val=ans[i]
            head=head.next
            i+=1
        return temp
            
        