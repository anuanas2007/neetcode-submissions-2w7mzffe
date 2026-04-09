class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cou1 = Counter(s)
        cou2 = Counter(t)

        if len(cou1) != len(cou2):
            return False

        for v,c in cou1.items():
            if v not in cou2:
                return False
            else:
                if cou1[v] != cou2[v]:
                    return False
            
        return True