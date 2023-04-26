class Solution {
    public static boolean is_possible_to_get_seats(int n, int m, int[] seats) {
        int maxSeats = (m+1)/2;
        if(n > maxSeats){
            return false;
        }
        int index = 0;
        while(index < m && n > 0){
            if(seats[index] == 0 && 
            (index == 0 || seats[index-1] != 1) 
            && (index == m-1 || seats[index+1] != 1)){
                seats[index] = 1;
                n--;
                index += 2;
            } 
            else{
                index++;
            }
        }
        return n == 0;
    }
}
   
