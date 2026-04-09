class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        cur = n

        while cur !=1:
            temp = 0
            while cur != 0:
                i = cur % 10
                cur = cur // 10
                temp += i * i
            if temp in seen:
                return False
            else:
                seen.add(temp)
                cur = temp
        
        return True