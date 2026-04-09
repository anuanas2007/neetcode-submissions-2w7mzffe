# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        queue = deque([root])

        def isSame(a,b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            return isSame(a.left, b.left) and isSame(a.right, b.right)

        while queue:
            n = queue.popleft()

            if n.val == subRoot.val:
                if isSame(n, subRoot):
                    return True
            
            if n.left:
                queue.append(n.left)
            
            if n.right:
                queue.append(n.right)
        
        return False



    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False

    #     if self.sameTree(root, subRoot):
    #         return True
        
    #     return (self.isSubtree(root.left, subRoot) or
    #            self.isSubtree(root.right, subRoot))
        
      
    # def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    #     if not root and not subRoot:
    #         return True

    #     if root and subRoot and root.val == subRoot.val:
    #         return (self.sameTree(root.left, subRoot.left) and
    #                self.sameTree(root.right, subRoot.right))
    #     return False 
        



        