
class Solution{
   static String longestPalin(String S){
       // code here
       String ans="";
       
       for(int i =0;i < S.length() ;i++){
           // tempLen is len of maximum palindrom starts with s[i]
           int tempLen = Palin(S,i);
           if(tempLen > ans.length()){
               if(tempLen==0){
                   tempLen=1;
               }
               ans=S.substring(i,i+tempLen);
           }
       }
       return ans;
       
       
   }
   static int Palin(String s,int start){
       int j = s.length() -1 ;
       int i = start;
       int len=0;
       // high is index of last charecter of currrent checking palindrome
       int high = j;
       while(j>start && i<s.length() && j>i){
           if(s.charAt(i) == s.charAt(j)){
               if(len==0){
                   high=j;
               }
               j--;
               i++;
               len+=2;
           }
           else{
// palindrome failed now again we'll start with i == start and last checking index will char just before we matched last in palindrome which failed
                   high--;
                   j=high;
//                    j--;

               i=start;
               len=0;
//                j=s.length()-1;
           }
       }
       if(j==i ){
           return len+1;
       }
       else{
           return len;
       }
   }
}
