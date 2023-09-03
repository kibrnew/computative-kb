class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans=0
        count=Counter(ages)
        for x in reversed(range(len(ages))):
            if ages[x]<=14:
                break
            y=x-bisect_right(ages,0.5 * ages[x] + 7)
            if count[ages[x]]>1:
                ans+=count[ages[x]]-1
                count[ages[x]]-=1
            ans+=y
        return ans
    