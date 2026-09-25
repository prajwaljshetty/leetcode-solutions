class Solution {
    public void rotate(int[][] matrix) {
        int[][] rotatedMatrix = new int[matrix.length][matrix[0].length];

        int columns = matrix.length , rows = matrix[0].length ; 
        for( int i = 0 ; i < columns ; i++ ){
            for( int j = 0 ; j < rows ; j++ ){
                rotatedMatrix[i][j] = matrix[ rows - j  - 1][ i ];
            }
        }

        for( int i = 0 ; i < columns ; i++ ){
            for( int j = 0 ; j < rows ; j++ ){
                matrix[i][j] = rotatedMatrix[i][j];
            }
        }
    }
}