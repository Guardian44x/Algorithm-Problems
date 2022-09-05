/*
$1353. Maximum Numbers of Events That Can Be Attended
*/

class Solution {
public:
    int maxEvents (vector<vector<int>>& events) {
        sort(events.begin(), events.end(), eventCompare);

        int n = events.size();
        int ans = 0;
        int i = 0;
        
        multiset<int> s;
        for (int d = 1; d < 100001; ++d) {
            while (!s.empty() && *(s.begin()) < d)
                s.erase(s.begin());
            while (i < n && events[i][0] == d) {
                s.insert(events[i][1]);
                ++i;
            }
            if (s.size() > 0) {
                ++ans;
                s.erase(s.begin());
            }
        }
        return ans;
    }

    static bool eventCompare(vector<int>& event1, vector<int>& event2) {
        return event1[0] != event2[0]? event1[0] < event2[0] : event1[1] < event2[1];
    }
};