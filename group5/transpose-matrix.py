class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # ans=[]
        # for val in zip(*matrix):
        #     ans.append(list(val))
        # return ans
        return list(zip(*matrix))
    
        
        