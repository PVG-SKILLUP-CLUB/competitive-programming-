# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution:

    def isSameTree(self, p, q):

        """

        :type p: TreeNode

        :type q: TreeNode

        :rtype: bool

        """    

        # p and q are both None

        if not p and not q:

            return True

        # one of p and q is None

        if not q or not p:

            return False

        if p.val != q.val:

            return False

        return self.isSameTree(p.right, q.right) and \

               self.isSameTree(p.left, q.left)
