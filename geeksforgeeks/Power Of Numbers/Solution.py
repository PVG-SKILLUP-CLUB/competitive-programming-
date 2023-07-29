class Solution:
   q=10**9+7
   def power(self,N,R):
       if R<=0:
           return 1
       return (N**(R&1)*self.power(N,R>>1)**2)%self.q
