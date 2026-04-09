class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        if len(edges) != n-1:
            return False

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()

        # def dfs(node, par):
        #     if node in visit:
        #         return False
            
        #     visit.add(node)
        #     for nei in graph[node]:
        #         if nei == par:
        #             continue
        #         if not dfs(nei, node):
        #             return False
                
        #     return True

        # return dfs(0, -1) and len(visit) == n
        

        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n
        
        