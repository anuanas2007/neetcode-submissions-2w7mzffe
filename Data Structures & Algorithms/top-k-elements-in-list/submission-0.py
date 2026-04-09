class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = []
        for _ in range(len(nums) + 1):
            freq.append([])

        for n, c in counter.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        