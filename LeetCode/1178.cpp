/*
$1178. Number of Valid Words for Each Puzzle
*/ 

class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        unordered_map<int, int> mp;
        for (auto w: words) {
            int mask = 0;
            for (auto a: w) 
                mask |= (1 << (a - 'a'));
            mp[mask]++;
        }
        vector<int> ans;
        for (auto p: puzzles) {
            int su = 0;
            for (auto a: p)
                su |= (1 << (a - 'a'));
            int mas = su;
            int first = (1 << (p[0] - 'a'));
            int co = 0;
            while (true) {
                if (((su & first) == first) && mp.find(su) != mp.end())
                    co += mp[su];
                if (su == 0)
                    break;
                su = (su - 1) & mas;
            }
            ans.push_back(co);
        }
        return ans;
    }
};