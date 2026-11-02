class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = -1;

        for(int i = 0 ; i < candies.size() ; i++){
            if(maxCandies < candies[i]) maxCandies = candies[i];
        }

        vector<bool> isGreater(candies.size() , false);

        for(int i = 0 ; i < candies.size()  ; i++){
            isGreater[i] = candies[i] + extraCandies >= maxCandies;
        }

        return isGreater;
    }
};