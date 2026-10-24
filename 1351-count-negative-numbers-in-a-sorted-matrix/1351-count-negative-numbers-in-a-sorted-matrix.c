int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int i = 0 , j = *gridColSize - 1 , count = 0;
    printf("%d",j);

    while( i < gridSize && j > -1 ){
        if(grid[i][j] < 0){
            count += (gridSize - i);
            j--;
        }else{
            i++;
        }
    }

    return count;
}