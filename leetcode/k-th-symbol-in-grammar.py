class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        k=k-1
        l=k.bit_length()
        target="0"*(n-l-1)+bin(k)[2:]

        if n==1:
            return 0
        


        def find(s,target):
            if len(target)==0:
                return s

            if s=="0":
                s="01"
            else:
                s="10"

            s=s[int(target[0])]

            return find(s,target[1:])

        return int(find("0",target))
            

        