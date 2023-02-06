class Solution:
    def compress(self, chars: List[str]) -> int:
        s=[]
        size=len(chars)
        pointer1=0
        pointer2=1
        count=1
        if len(chars)==1:
            s.append(chars[0])
            return 1
        while pointer2<size:
            if chars[pointer1]==chars[pointer2]:
                pointer2 +=1
                count +=1
            else:
                if count>1:
                    s.append(chars[pointer1])
                    s.extend(list(str(count)))
                else:
                    s.append(chars[pointer1])
                pointer1=pointer2
                pointer2+=1
                count=1
            if pointer2==size: 
                if count>1 :
                    s.append(chars[pointer1])
                    s.extend(list(str(count)))               
                else:
                    s.append(chars[pointer1])
                
        chars[0:] = s 
        return len(s)
                
                
                
            
        