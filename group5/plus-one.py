class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[str(i) for i in digits]
        num="".join(l)
        new=list(str(int(num)+1))
        return [int(i) for i in new]
