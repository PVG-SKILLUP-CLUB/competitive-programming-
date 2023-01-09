# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ls=[]

        def dfs(root):

            if not root:

                return

            ls.append(root.val)

            dfs(root.left)

            dfs(root.right)

        dfs(root)

        return ls
