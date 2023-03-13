# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:return True

        stack = [(root.left, root.right)] 

        while stack: 

            cur = stack.pop()

            l, r = cur[0], cur[1] 

            if not l and not r:continue 

            if not l and r or not r and l or l.val != r.val:

                return False 

            stack.append((l.right, r.left)) 

            stack.append((l.left, r.right)) 

        return True
