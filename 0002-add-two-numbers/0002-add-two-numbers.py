# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=[]
        temp2=[]
        while l1.next:
            temp1.append(str(l1.val))
            l1=l1.next
        temp1.append(str(l1.val))
        l1=l1.next
        while l2.next:
            temp2.append(str(l2.val))
            l2=l2.next
        temp2.append(str(l2.val))
        l2=l2.next
        
        ans1=int("".join(temp1[::-1]))
        ans2=int("".join(temp2[::-1]))
        ans=str(ans1+ans2)[::-1]
        new0=ListNode(int(ans[0]))
        head=new0
        for i in ans[1:]:
            new=ListNode(int(i))
            new0.next=new
            new0=new
        return head
        
        