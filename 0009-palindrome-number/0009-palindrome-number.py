class Solution:
    def isPalindrome(self, x: int) -> bool:
        new=str(x)
        if new==new[::-1]:
            return True
        return False
        