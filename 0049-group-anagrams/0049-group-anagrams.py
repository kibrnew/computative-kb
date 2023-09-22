class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            stor=defaultdict(list)
            n=len(strs)
            def count(val):
                t=Counter(val)
                temp=[]
                k=sorted(t.keys())
                for key in k:
                    temp.append(key+str(t[key]))
                return "".join(temp)
            for word in strs:
                temp=count(word)
                stor[temp].append(word)
            return list(stor.values())
            
                
                    