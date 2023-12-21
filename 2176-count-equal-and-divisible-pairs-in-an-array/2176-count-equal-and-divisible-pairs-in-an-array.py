class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        ind=defaultdict(list)
        n=len(nums)
        for i in range(n):
            
            ind[nums[i]].append(i)
            
        ans=0
        
        for val in ind.values():
            
            temp=0
            visted=set()
            for i in range(len(val)):
                left=val[i]
                
                for j in range(i+1,len(val)):
                    right=val[j]
                    if right*left%k==0:
                        temp+=1
            ans+=temp
        return ans