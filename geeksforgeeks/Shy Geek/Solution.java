class Solution{
    
    static Shop shop;
    Solution(Shop shop){
        this.shop = shop;
    }
        static long find(int n, long k){
        long count = 0;
        int left = 0, right = n-1;
        
        // iterate until we spend our whole money
        while(k > 0){
            // placeholder to get max. choco price for curreny money{k} that we have
            int currMax = -1;
            
            // find max cost using Binary Search and assign it to {currMax}
            while(left <= right){
                int mid = (left+right)/2;
                int cost = shop.get(mid);
                
                if(cost > k){
                    // geek can not afford to buy
                    right = mid-1;
                } else {
                    // geek can buy and this cost might be a possible ans, but we will check for bigger
                    currMax = cost;
                    left = mid+1;
                }
            }
            // if no cost found, we got our ans, {or all the chocos are more costly than current* {k} value}
            if(currMax == -1) break;
            
            // count the no. of choco we can buy with {currMax}
            count += k/currMax;
            
            // update the rest coins left after buying
            k = k%currMax;
            
            // set low pointer to {0}, 
            // no need to set high pointer to end of the array as we can not afford those choco
            left = 0;
        }
        
        return count;
    }
}
