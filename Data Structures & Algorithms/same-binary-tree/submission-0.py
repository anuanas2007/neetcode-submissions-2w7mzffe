# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p:
            if q:
                return False
            if not q:
                return True
        
        if not q:
            if p:
                return False
        
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        while q1 or q2:
            cur1 = q1.popleft()
            cur2 = q2.popleft()

            if cur1.val != cur2.val:
                return False

            if cur1.left or cur2.left:
                if not cur2.left:
                    return False
                if not cur1.left:
                    return False
                q1.append(cur1.left)
                q2.append(cur2.left)
            
            if cur1.right or cur2.right:
                if not cur2.right:
                    return False
                if not cur1.right:
                    return False
                q1.append(cur1.right)
                q2.append(cur2.right)
        
        return not q1 and not q2
            
        