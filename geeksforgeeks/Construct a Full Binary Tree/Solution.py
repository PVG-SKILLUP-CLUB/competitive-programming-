
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        if len(pre) == 0:
            return None
        root = Node(pre[0])
        mid = len(pre) // 2
        root.left = self.constructBinaryTree(pre[1:mid+1], preMirror,size)
        root.right = self.constructBinaryTree(pre[mid+1:], preMirror, size)
        return root
