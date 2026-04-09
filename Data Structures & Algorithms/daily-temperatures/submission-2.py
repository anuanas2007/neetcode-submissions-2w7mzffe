class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0] * l
        stack = []

        for i in range(l):
            ind = l - i - 1
            while stack and stack[-1][0] <= temperatures[ind]:
                stack.pop()
            if stack:
                res[ind] = stack[-1][1] - ind
            
            stack.append([temperatures[ind],ind])
        
        return res


