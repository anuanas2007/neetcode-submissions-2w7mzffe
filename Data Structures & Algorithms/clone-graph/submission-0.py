"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Map original node -> cloned node
        clones = {}

        # Start BFS
        queue = deque([node])

        # Clone the first node
        clones[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in clones:
                    # Clone neighbor
                    clones[nei] = Node(nei.val)
                    queue.append(nei)

                # Add cloned neighbor to cloned current node
                clones[curr].neighbors.append(clones[nei])

        return clones[node]
        