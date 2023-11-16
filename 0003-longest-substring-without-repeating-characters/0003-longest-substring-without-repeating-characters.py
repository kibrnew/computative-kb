class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pr1=0
        temp=set()
        length=0
        if not s:
            return 0
        for i in range(len(s)):
            if not s[i] in temp:
                temp.add(s[i])
                length=max(length,len(temp))
            else :
                while s[i] in temp:
                    temp.remove(s[pr1])
                    pr1+=1
                temp.add(s[i])
        return length
                