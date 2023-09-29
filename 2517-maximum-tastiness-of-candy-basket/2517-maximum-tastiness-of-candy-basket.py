class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        L = 0
        R = (price[-1] - price[0]) // (k - 1)
        while L < R:
            M = (L + R + 1) >> 1
            x = 0
            y = price[0]
            for t in price:
                if t >= y:
                    x += 1
                    y = t + M
            if x < k: R = M - 1
            else: L = M
        return L