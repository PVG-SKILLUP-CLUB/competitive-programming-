from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def LCA(root, n1, n2):
    if root is None:
        return None

    # If both n1 and n2 are greater than root, LCA lies in the right subtree
    if root.data < n1 and root.data < n2:
        return LCA(root.right, n1, n2)

    # If both n1 and n2 are less than root, LCA lies in the left subtree
    if root.data > n1 and root.data > n2:
        return LCA(root.left, n1, n2)

    # If the current node's value lies between n1 and n2, then it's the LCA
    return root

# Function to Build Tree   
def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None
        
    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))                     
    size = 0
    q = deque()
    
    q.append(root)
    size = size + 1 
    
    i = 1                                       
    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size = size - 1
        
        currVal = ip[i]
        
        if currVal != "N":
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size = size + 1
        
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    
    return root
