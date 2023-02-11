class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        ans=[]
        half=(len(arr)+1)//2
        final=0
        summ=0
        count=1
        cur=arr[0]
        for i in range(1,len(arr)):
            if cur== arr[i]:
                count+=1
            else :
                ans.append(count)
                cur=arr[i]
                count=1
            if i==len(arr)-1:
                ans.append(count)
                cur=arr[i]
                count=1
        ans.sort()  
        for i in range(len(ans)):
            temp=ans[-1]
            summ+=temp
            final+=1
            ans.pop()
            if half<=summ:
                break
        return final