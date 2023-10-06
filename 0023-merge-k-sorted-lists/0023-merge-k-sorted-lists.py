# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(h1,h2):
            cur=ListNode(-float("inf"))
            ans=cur
            while h1 and h2:
                if h2.val>=h1.val:
                    cur.next=h1
                    cur=cur.next
                    h1=h1.next
                else:
                    cur.next=h2
                    cur=cur.next
                    h2=h2.next
            if not h1:
                cur.next=h2
            else:
                cur.next=h1
            return ans.next  
        def merge_sort(l):
            if len(l)<2:
                if not l:
                    return None
                return l[0]
            else:
                middle=len(l)//2
                left=merge_sort(l[:middle])
                right=merge_sort(l[middle:])
                return merge(left,right)
        
        return merge_sort(lists)
        
                
                