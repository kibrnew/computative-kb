class Solution:
    def findLength(self, nums1a: List[int], nums2b: List[int]) -> int:  
        def check(nums1,nums2):
            n=len(nums1)
            m=len(nums2)
            ans=0
            for i,first in enumerate(nums1):
                left=0
                w=0
                while left<m:
                    w=0
                    if first==nums2[left]:
                        while left+w<m and i+w<n and nums1[i+w]==nums2[left+w]:
                            w+=1
                        ans=max(ans,w)
                        if nums1[i+w-1]==nums2[left+w-1]:
                            w-=1
                        left+=w
                    left+=1
            return ans 
        return max(check(nums1a,nums2b),check(nums2b,nums1a))

                
            
        
        