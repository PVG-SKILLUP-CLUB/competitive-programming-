# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        nodeValues = []

        def dfs(node):

            if node is None:

                return

            nodeValues.append(node.val)

            dfs(node.left)

            dfs(node.right)

        

        dfs(root)

        nodeValues.sort()

        minDifference = 1e9

        for i in range(1, len(nodeValues)):

            minDifference = min(minDifference, nodeValues[i] - nodeValues[i-1])

        return minDifference
