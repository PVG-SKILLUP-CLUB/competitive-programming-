class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
     def ladoos(self, root, home, k):
        
        ans = 0
        def sum_node(n, k):
            nonlocal ans
            if not n or k < 0:
                return 0
            ans += n.data 
            sum_node(n.left, k-1)
            sum_node(n.right, k-1)
            

        def walk(n):
            nonlocal ans, k
            if not n:
                return False, 0
            if n.data == home:
                sum_node(n, k)
                return True, k-1
            
            flag, left = walk(n.left)
            if flag and left >= 0:
                ans += n.data
                sum_node(n.right, left-1)
                return flag, left-1
            
            flag, right = walk(n.right)
            if flag and right >= 0:
                ans += n.data
                sum_node(n.left, right-1)
                return flag, right-1
            
            return False, 0
        walk(root)
        return ans


