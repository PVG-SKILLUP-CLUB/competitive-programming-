class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self, root):
       if(not root):
           return []
       ans = []
       ans.append(root.data)
       self.rightTrav(root, ans, 1)
       return ans
       
    def rightTrav(self, root, ans, level):
       
       if(not root):
           return
       
       if(level == len(ans)):
           if(root.right):
               ans.append(root.right.data)
           elif(root.left):
               ans.append(root.left.data)
       
       self.rightTrav(root.right, ans, level+1)
       self.rightTrav(root.left, ans, level+1)
      
