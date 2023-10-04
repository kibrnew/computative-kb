class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst = []

        for ele in nums:
            lst += [str(ele)]
        print(lst)
        n = len(lst)

        for i in range(n):
            for j in range(i+1 , n):
                
                if str(lst[i]) + str(lst[j]) > str(lst[j]) + str(lst[i]):
                    # if current order is greatest value .. continue
                    continue
                else:
                    # else swap the values ..!!!
                    lst[i] , lst[j] = lst[j] , lst[i]
        
        
        ans = ''.join(lst)

        if int(ans) == 0:
            return "0"
        
        return ans


        
        
#         k=[str(i) for i in nums]
#         k.sort(reverse=True)
#         ans=[[k[0]]]
#         i=0
#         for j in range(1,len(k)):
#             if k[j][0]==k[j-1][0]:
#                 ans[i].append(k[j])
#             else:
#                 ans.append([k[j]])
#                 i+=1
#         def sorter(x):
#             ad=l-len(x)
#             n=x+x*((ad//len(x))+1)
#             mm=n[:l]
            
#             return -int(mm)
#         final=[]
#         for lis in ans :
#             m=max(lis,key=lambda x:int(x))
#             l=len(m)
#             lis.sort(key=sorter)
#             final.append("".join(lis))
#         return "".join(final)