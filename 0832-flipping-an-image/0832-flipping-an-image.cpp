class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int length , mid;

        for(int i = 0 ; i < image.size() ; i++){
            length = image[i].size() - 1;
            mid = (length / 2);
            for(int j = 0 ; j < mid + 1 ; j++){
                int temp = image[i][j] ? 0 : 1;
                image[i][j] = image[i][length - j] ? 0 : 1;
                image[i][length - j] = temp;
            }
        }

        return image;
    }
};