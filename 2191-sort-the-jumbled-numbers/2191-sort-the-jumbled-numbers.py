class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def sorter(x):
            s=str(x)
            new=[]
            for val in s:
                new.append(str(mapping[int(val)]))

            return int("".join(new))

        return sorted(nums,key=sorter)
        