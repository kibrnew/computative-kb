class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        

        ind={}
        for i in range(len(order)):
            ind[order[i]]=i
        
        # new=sorted(words,key=lambda word:[ind[i] for i in word])
        # return new==words
    
        prev=words[0]
        for word in words[1:]:
            if max(word,prev,key=lambda word:[ind[i] for i in word])!=word:
                return False
            prev=word
        return True
            
        
        
        
        
        
#         def compare(a,b):
#             n=len(a)
#             m=len(b)
#             for i in range(min(n,m)):
#                 if ind[a[i]]<ind[b[i]]:
#                     return a 
#                 elif ind[a[i]]>ind[b[i]]:
#                     return b
#             if m>n:
#                 return a
#             else:
#                 return b
            
                
#         n=len(words)
#         ans=words[::]
#         for i in range(n):
#             mini=ans[i]
#             for j in range(i+1,n):
#                 if compare(mini,ans[j])!=mini:
#                     mini,ans[j]=ans[j],mini
#                     return False
#         return True
                    
                
                
        