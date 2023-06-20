class Solution {
   static int matchGame(Long N) {
       if(N%5 == 0) { 
           return -1;
       }
       int ans = (int)(N%5);
       return ans;
   }
};
