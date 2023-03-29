class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            count = sum(i)
            if count > ans:
                ans = count
        return ans
        