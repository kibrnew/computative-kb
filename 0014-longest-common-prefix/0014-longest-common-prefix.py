class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        store=strs[0]
        j=0
        for word in strs:
            while j<len(word) and j<len(store):
                if word[j]==store[j]:
                    j+=1
                else:
                    break 
            store=word[:j]
            j=0
        return store
                    
                    
            
            
        