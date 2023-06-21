class Solution {
    static int sumOfNaturals(int n) {
        // code here
            long bi = 0;
        for(int i=1 ; i<=n ; i++){
            bi += i;
        }
        return (int)(bi%(1000000007));
    }
};
