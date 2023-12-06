class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        
        ans=[]
        # print(row1)
        for wordi in words:
            word=wordi.lower()
            flag=False
            if word[0] in row1:
                for c in word:
                    if c not in row1:
                        flag=True
                        break
                    
            elif word[0] in row2:
                for c in word:
                    if c not in row2:
                        flag=True
                        break
                        
            elif word[0] in row3:
                for c in word:
                    if c not in row3:
                        flag=True
                        break
            if not flag:
                ans.append(wordi)
        return ans
                
        