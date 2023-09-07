class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=defaultdict(int)
        n=len(position)
        for i in range(n):
            time[position[i]]=(target-position[i])/speed[i]
        position.sort()
        ans=[time[position[0]]]

        for i in range(1,n):
            temp=time[position[i]]
            if temp<ans[-1]:
                ans.append(temp)
            else:
                while ans and ans[-1]<=temp:
                    ans.pop()
                ans.append(temp)
        return len(ans)
        