/*
$1131. Maximum of Absolute Value Expression
*/

class Solution {
public:
    int maxAbsValExpr (vector<int>& arr1, vector<int>& arr2) {
        int n = arr1.size();
        vector<int> sum1(n, 0), diff1(n, 0), sum2(n, 0), diff2(n, 0);
        for (int i = 0; i < n; ++i) {
           sum1[i] = arr1[i] + arr2[i] + i;
           diff1[i] = arr1[i] - arr2[i] + i;
           sum2[i] = arr1[i] + arr2[i] - i;
           diff2[i] = arr1[i] - arr2[i] - i;
        } 
        int max_vals[4] = {sum1[0], diff1[0], sum2[0], diff2[0]};
        int min_vals[4] = {sum1[0], diff1[0], sum2[0], diff2[0]};
        for (int i = 0; i < n; ++i) {
            max_vals[0] = max(max_vals[0], sum1[i]);
            max_vals[1] = max(max_vals[1], diff1[i]);
            max_vals[2] = max(max_vals[2], sum2[i]);
            max_vals[3] = max(max_vals[3], diff2[i]);
            min_vals[0] = min(min_vals[0], sum1[i]);
            min_vals[1] = min(min_vals[1], diff1[i]);
            min_vals[2] = min(min_vals[2], sum2[i]);
            min_vals[3] = min(min_vals[3], diff2[i]);
        }
        int ans = 0;
        for (int i = 0; i < 4; ++i)
            ans = max(ans, max_vals[i] - min_vals[i]);
        return ans;
    }
};