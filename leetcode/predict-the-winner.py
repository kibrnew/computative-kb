class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        arr=nums
        def winner(l,r):

            if r-l+1==1:
                return arr[l]
            if r-l+1==2:
                return max(arr[l:r+1])
            

            first=arr[l]

            # rem=arr[l+2:r]
            # rem2=arr[l+1:r-1]

            v1=first+min(winner(l+2,r),winner(l+1,r-1))

            last=arr[r]

            # rem=arr[l+1:r-1]
            # rem2=arr[l:r-2]

            v2= last+min(winner(l+1,r-1),winner(l,r-2))

            return max(v1,v2)

        player1=winner(0,len(nums)-1)
        player2=sum(nums)-player1
        
        return player1>=player2

        