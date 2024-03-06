class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # ind=bisect_right(letters,target)


        
        l=-1
        r=len(letters)

        while l+1<r:
            mid=l+(r-l)//2
            if letters[mid]<=target:
                l=mid
            else:
                r=mid
        if r>=len(letters):
            r=0
        return letters[r]


        