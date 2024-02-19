# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        
        l=n//k
        res=[l]*k
        n-=l*k
        for i in range(n):
            res[i]+=1
        ans=[]
    
        temp=head
        for val in res:
            if val==0:
                ans.append(None)
                continue 
            new=temp
            for i in range(val-1):
                temp=temp.next
            cur=temp.next
            temp.next=None
            ans.append(new)
            temp=cur
        return ans 
            
                
        
            
        