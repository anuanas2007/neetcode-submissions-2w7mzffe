# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, gre):
            good = 0
            stack = []
            stack.append([node, gre])
            while stack:
                n,g = stack.pop()
                if n.val >= g:
                    good += 1
                    g = n.val
                
                if n.left:
                    stack.append([n.left, g])
                
                if n.right:
                    stack.append([n.right, g])

            return good

        return dfs(root, float('-inf'))