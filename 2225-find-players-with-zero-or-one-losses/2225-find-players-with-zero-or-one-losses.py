class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        count=defaultdict(int)
        
        for w,l in matches:
            
            count[w]+=0
            count[l]+=1
            
        
        one=[]
        zero=[]
        
        for key,val in count.items():
            if val==1:
                one.append(key)
            if val==0:
                zero.append(key)
        return [sorted(zero),sorted(one)]
            
        
                