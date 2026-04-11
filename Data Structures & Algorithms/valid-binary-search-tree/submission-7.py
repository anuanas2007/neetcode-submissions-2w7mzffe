# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append([root, float("-inf"), float("inf")])

        while q:
            cur, l, r = q.popleft()
            print(cur.val,l,r)

            if not (l < cur.val < r):
                return False
            
            if cur.right:
                q.append([cur.right, cur.val, r])
            
            if cur.left:
                q.append([cur.left, l, cur.val])
        
        return True

        
            

        