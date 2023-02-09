class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        size=len(citations)
        for i in range(len(citations)):
            if citations[i] >= size-i :
                return size-i
            
        return 0