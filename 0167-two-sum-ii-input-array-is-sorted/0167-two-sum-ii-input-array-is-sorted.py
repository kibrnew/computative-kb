class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pr1=0
        pr2=len(numbers)-1
        while pr1<pr2:
            if (numbers[pr1]+numbers[pr2])==target:
                return [pr1+1,pr2+1]
            if (numbers[pr1]+numbers[pr2])<target:
                pr1+=1
            if (numbers[pr1]+numbers[pr2])>target:
                pr2-=1
        