# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0 # no node edge case 
            left = right = float(inf) 
            if node.left: left = dfs(node.left) # if there's left leg, visit it 
            if node.right: right = dfs(node.right) # if there's right leg, visit it
            if node.left == node.right: return 1 # we are at a leaf node, return 1
            return min(left, right) + 1 # pick min of both legs + 1
        return dfs(root)
