# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        nums=[]
        temp=head
        while temp:
            nums.append(temp.val)
            temp=temp.next
            
        left=[]
        right=[]
        for val in nums:
            if val>=x:
                right.append(val)
            else:
                left.append(val)
        new=left+right
        
        temp=head
        i=0
        while head:
            head.val=new[i]
            i+=1
            head=head.next
        return temp
        