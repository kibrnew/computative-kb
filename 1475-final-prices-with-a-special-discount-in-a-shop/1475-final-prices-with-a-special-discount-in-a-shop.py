class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack=[]
        for i in range(len(prices)):
            if not stack:
                stack.append(i)
            else:
                while stack and prices[stack[-1]]>=prices[i]:
                    prices[stack.pop()]-=prices[i]
                stack.append(i)
        return prices
            
            
            
        