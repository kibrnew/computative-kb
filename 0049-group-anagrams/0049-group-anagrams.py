class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            stor=defaultdict(list)
            n=len(strs)
            for word in strs:
                temp=sorted(word)
                stor["".join(temp)].append(word)
            return list(stor.values())
            
                
                    