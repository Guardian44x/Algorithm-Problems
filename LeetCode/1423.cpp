/*
$1423. Maximum Points You Can Obtain from Cards.
*/

class Solution {
public: 
    int maxScore(vector<int>& cardPoints, int k) {
        int total_sum = 0;
        for (int i = 0; i < cardPoints.size(); i++)
            total_sum += cardPoints[i];
        int n = cardPoints.size();
        int sub_sum = 0;
        for (int i = 0; i < n-k; i++)
            sub_sum += cardPoints[i];
        int min_sub_sum = sub_sum;
        for (int i = n-k; i < cardPoints.size(); i++) {
            sub_sum = sub_sum + cardPoints[i] - cardPoints[i-(n-k)];
            min_sub_sum = min(sub_sum, min_sub_sum);
        }
        return total_sum - min_sub_sum;
    }
};