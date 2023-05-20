class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum= ''
        for i in range(97, 123):
            alphanum+= chr(i)
        for i in range(48, 58):
            alphanum+= chr(i)
        print(alphanum)
        new=s.lower()
        ans=""
        for i in new :
            if i in alphanum:
                ans+=i
        return ans==ans[::-1]