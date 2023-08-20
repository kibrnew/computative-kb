class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        cur=[-i for i in count.values()]
        heapify(cur)
        stat=deque()
        ans=0
        print(cur)
        while cur or stat:
            ans+=1
            if cur:
                now=-heappop(cur)-1
                if now>0:
                    stat.append((ans+n,now))
            if stat and stat[0][0]==ans:
                add=stat.popleft()[1]
                heappush(cur,-add)
           
        return ans
        