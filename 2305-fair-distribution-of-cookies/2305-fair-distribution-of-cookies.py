class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        n = len(cookies)
        result = [float('inf')] 
        def dfs(i, cur):
            if i == n:
                result[0] = min(result[0], max(cur))
                return
            if result[0]<=max(cur):
                return
            for j in range(k):
                cur[j] += cookies[i]
                dfs(i + 1, cur)
                cur[j] -= cookies[i]

        dfs(0, [0] * k)
        return result[0]
