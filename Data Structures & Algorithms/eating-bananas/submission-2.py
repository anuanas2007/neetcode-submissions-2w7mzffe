class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = len(piles)

        if l >= h:
            return max(piles) 
        
        def canFinish(no):
            time = 0
            for i in piles:
                if i < no:
                    time += 1
                elif i % no == 0:
                    time += i//no
                else:
                    time += (i//no) + 1
            
            if time <= h:
                return True
            else:
                return False

        m = max(piles)
        res = m

        l, r = 1, m

        while l <= r:
            n = (l+r)//2

            if canFinish(n):
                res = min(res, n)
                r = n - 1
            
            else:
                l = n + 1
        
        return res


        