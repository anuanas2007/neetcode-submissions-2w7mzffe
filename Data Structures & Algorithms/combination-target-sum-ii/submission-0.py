class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= n or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i+1, cur, total)



        dfs(0, [], 0)
        return res   
        



        # res = []
        # candidates.sort()

        # def helper(start, target, subset):
        #     if target == 0:
        #         res.append(subset.copy())
        #         return
            
        #     for i in range(start,len(candidates)):

        #         if i > start and candidates[i] == candidates[i-1]:
        #             continue
                    
        #         if candidates[i] > target:
        #             break
               
        #         subset.append(candidates[i])
        #         helper(i+1, target-candidates[i],subset)
        #         subset.pop()
        

        # helper(0, target, [])
        # return res
        