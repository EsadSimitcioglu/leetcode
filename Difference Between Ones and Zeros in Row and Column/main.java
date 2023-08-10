class Solution {

    public int getRow(int[][] grid, int selectedNumber, int i) {
        int count = 0;
        for(int number : grid[i]) {
            if (number == selectedNumber){
                count++;
            }
        }
        return count;
    }

    public int getCol(int[][] grid, int selectedNumber, int j) {
        int count = 0;

        for (int[] rows : grid) {
            if (rows[j] == selectedNumber) {
                count++;
            }
        }
        return count;
    }

    public int[][] onesMinusZeros(int[][] grid) {

        HashMap<Integer, Integer> columnCounterOne = new HashMap<>();
        HashMap<Integer, Integer> columnCounterZero = new HashMap<>();

        for(int j=0;j<grid[0].length;j++){
            int b = getCol(grid, 1, j);
            columnCounterOne.put(j, b);
            int d = grid[0].length-b;
            columnCounterZero.put(j, d);
        }

        int [][] diffGrid = new int[grid.length][grid[0].length];

        for(int i =0;i<grid.length;i++){
            int a = getRow(grid, 1, i);
            int c = grid.length-a;

            for(int j=0;j<grid[i].length;j++){
                int b = columnCounterOne.get(j);
                int d = columnCounterZero.get(j);

                diffGrid[i][j] = a + b - c - d;
            }
        }
        return diffGrid;
    }

}