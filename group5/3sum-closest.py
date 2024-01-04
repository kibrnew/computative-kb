class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
    
        n=len(nums)
        diff=float("inf")
        pol=1
        nums.sort()
        for i in range(n):
            left=i+1
            right=n-1
            k=target-nums[i]
            
            while left<right:
                s=nums[left]+nums[right]
                if s>k:
                    if diff>s-k:
                        diff=s-k
                        pol=1
                    right-=1
                    
                else:
                    
                    if diff>k-s:
                        diff=k-s
                        pol=-1
                    left+=1
                # print(diff)
                    
            
        return target+diff*pol
                    

                
        