class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        temp=set()
        
        container=set(list1)
        
        for val in list2:
            if val in container:
                temp.add(val)
        
        value=defaultdict(int)
        for i,val in enumerate(list1):
            if val in temp:
                value[val]+=i
        for i,val in enumerate(list2):
            if val in temp:
                value[val]+=i
        mini=min(value.values())
        
        ans=[]
        for key,val in value.items():
            if val==mini :
                ans.append(key)
        return ans