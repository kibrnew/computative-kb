class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pos= [i for i, char in enumerate(s) if char == "|"]
        final = []
        for start, end in queries:
            left = bisect_left(pos,start)
            right = bisect_left(pos,end + 1)- 1
            answer = pos[right] - pos[left] - (right - left) if left < right else 0
            final.append(answer)
        return final

