
class Solution {
    static int shortestXYDist(ArrayList<ArrayList<Character>> grid, int N, int M) {
        List<int[]> x = new ArrayList<>(); // store all X with their co-ordinates
        List<int[]> y = new ArrayList<>(); // store all Y with their co-ordinates
        int distance = Integer.MAX_VALUE;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(grid.get(i).get(j) == 'X') x.add(new int[]{i, j});
                else if(grid.get(i).get(j) == 'Y') y.add(new int[]{i, j});
            }
        }
        // for every x, calculate manhattan distance with all Y, and store minimum distance in answer variable
        for(int[] xi : x) {
            for(int[] yi : y) {
                distance = Math.min(distance, Math.abs(xi[0]-yi[0]) + Math.abs(xi[1]-yi[1]));
            }
        }
        return distance;
    }
};
