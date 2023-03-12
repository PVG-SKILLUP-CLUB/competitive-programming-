class Solution {

    public int[] findMaxRow(int mat[][], int N) {

        int rowNum = 0, maxNum = 0;

        int index = N - 1;

        for (int i = 0; i < N; i++) {

            while (index >= 0 && mat[i][index] == 1) {

                index--;

                maxNum++;

                rowNum = i;

            }

        }

        return new int[] {rowNum, maxNum};

    }

};
