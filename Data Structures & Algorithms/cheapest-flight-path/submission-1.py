class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        prices[src] = 0

        adj = [[] for _ in range(n)]

        for u, v, cst in flights:
            adj[u].append([v, cst])
        
        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue
            
            for nei, w in adj[node]:
                c = cst + w
                if c < prices[nei]:
                    prices[nei] = c
                    q.append((c,nei,stops+1))
        
        return prices[dst] if prices[dst] != float("inf") else -1


        # prices = [float("inf")] * n
        # prices[src] = 0

        # for i in range(k+1):
        #     tmp = prices.copy()

        #     for s, d, p in flights:
        #         if prices[s] == float("inf"):
        #             continue
        #         if prices[s] + p < tmp[d]:
        #             tmp[d] = prices[s] + p
            
        #     prices = tmp
        
        # if prices[dst] == float("inf"):
        #     return -1
        # else:
        #     return prices[dst]