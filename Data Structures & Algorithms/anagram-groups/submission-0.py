class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}

        for i in strs:
            s = str(sorted(i))
            if s not in check:
                check[s] = []
            check[s].append(i)
        
        res =[]
        for a,v in check.items():
            res.append(v)
        
        return res