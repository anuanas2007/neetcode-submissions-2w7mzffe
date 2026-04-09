class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        pro = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                pro = max(pro, prices[r]-prices[l])
            else:
                l = r
            r += 1
        
        return pro
    
