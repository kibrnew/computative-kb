class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.strip().split(" ")
        return len(k[-1])
        