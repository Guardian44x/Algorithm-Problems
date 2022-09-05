/*
$219. Contains Duplicate II
*/

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> k_pre_count;
        for (int i = 0; i < nums.size(); i++) {
            if (k_pre_count.find(nums[i]) == k_pre_count.end()) {
                k_pre_count[nums[i]] = 1;
            } else {
                k_pre_count[nums[i]] ++;
                if (k_pre_count[nums[i]] > 1)
                    return true;
            }
            if (i >= k)
                k_pre_count[nums[i-k]] --;
        }
        return false;
    }
};


class Solution2 {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        for(int i=0; i<nums.size();i++){
            if(m.find(nums[i]) == m.end()) m[nums[i]] =i;
            else {
                if (i - m[nums[i]] <= k) return true;
                else m[nums[i]] = i;
            }
        }
        return false;
    }
};