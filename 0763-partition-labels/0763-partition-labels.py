class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        w=[]
        ans=[]
        size=len(s)
        pr1=0
        for i in range(size):
            w.append(s.rfind(s[i]))
        pr2=w[0]
        while pr2<size:
            if pr1==pr2:
                ans.append(pr1)
                if (pr2+1)==size:
                    break
                pr1+=1
                pr2=w[pr1]
            while pr1<pr2:
                if w[pr1]>pr2:
                    pr2=w[pr1]
                    pr1=0
                    break
                pr1+=1
                #if pr1+1 == pr2:
                  #  ans.appen(pr1)
                
                
        ans2=[]
        for i in range(len(ans)):
            if i==0:
                ans2.append(ans[0]+1)
            else:
                ans2.append(ans[i]-ans[i-1])
                
        return ans2
                
            
            