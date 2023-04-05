class Solution {
     public int countSpecialNumbers(int N, int arr[]) {
        // Code here
        int max = -1;
        
        // finding max
        for(int n : arr){
            max = Math.max(max, n);
        }
        
        //creating array of {max+1) length
        int[] hash = new int[max+1];
        int len = hash.length;
        
        //increasing value of {hash} array for each input array multiples
        for(int i=0; i<N; i++){
            int start = arr[i];
            if(hash[start] <= 1){
                for(int j=start; j<len; j=j+start){
                    hash[j]++;
                }
            }
        }
        int ans = 0;
        
        // cheking in hash array if it has more than 1 divider,
        // if yes, ans++
        for(int i=0; i<N; i++){
            if(hash[arr[i]] > 1) ans++;
        }
        return ans;
    }
    
}
