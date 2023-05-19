class Solution {
    public static ArrayList<Integer> kthSmallestNum(int n, int[][] r, int qn, int[] q) {
       ArrayList<Integer> res = new ArrayList<>();
       Arrays.sort(r, (a, b)->a[0] != b[0] ? a[0]-b[0]: b[1]-a[1]);
       
       for(int quer : q){
           int temp = util(r, quer);
            res.add(temp);
       }
       return res;
       
    }
    public static int util(int[][] range, int k) {
        int i = 1;
        if(k <= range[0][1]-range[0][0]+1) return  range[0][0]+k-1;
        k = k-(range[0][1]-range[0][0]+1);
        int prevEnd = range[0][1];
        while(i<range.length){
            // System.out.println(prevEnd+" "+k);
            if(prevEnd < range[i][0]){
                prevEnd  = range[i][0];
            }else{
                prevEnd++;
            }
                    if(k <= range[i][1]-prevEnd+1){
                        return prevEnd+k-1;
                    }else{
                        k = k-(range[i][1]-prevEnd+1);
                    }
            prevEnd  = range[i][1];
            i++;
        }
        return -1;
       
    }
}
