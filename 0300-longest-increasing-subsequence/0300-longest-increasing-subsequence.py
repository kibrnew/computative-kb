class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                # print(sub,"before appending")
                sub.append(x)
                # print(sub,"after appending")
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                # print(sub,"before replacing the number")
                sub[idx] = x  # Replace that number with x
                # print(sub,"after replacing the number")
        # print(sub)
        return len(sub)
        