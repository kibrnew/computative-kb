class Solution:
    def addDigits(self, num: int) -> int:
        
        def digit(n):
            if n<10:
                return n
            return digit( sum([int(i) for i in list(str(n))]) )
        return digit(num)