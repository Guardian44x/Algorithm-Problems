/*
$514. Freedom Trail
*/

class Solution {
public:
    int findRotateSteps(string ring, string key) {
        vector<int> pos[26];
        int r = ring.size(), k = key.size();
        for(int i=0;i<r;i++) pos[ring[i]-'a'].push_back(i);
        vector<vector<int>> dp(k+1,vector<int>(r,INT_MAX));
        dp[k].assign(r,0);
        for(int i=k-1;i>=0;i--) 
            for(int j=0;j<r;j++)
                for(int nxt:pos[key[i]-'a']) {
                    int dist = abs(j-nxt);
                    dp[i][j]=min(dp[i][j],min(dist,r-dist)+dp[i+1][nxt]);
                }
        return dp[0][0]+k;
    }
};