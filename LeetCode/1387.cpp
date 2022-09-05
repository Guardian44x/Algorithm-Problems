/*
$1387. Sort Integers by The Power Value
*/

class Solution {
public:
    int getKth (int lo, int hi, int k) {
        int * nums;
        nums = new int[hi-lo+1];
        for(int i=0; i<hi-lo+1; i++)
            nums[i] = i + lo;
        sort(nums, nums+hi-lo+1, powerCompare);
        int ans = nums[k-1];
        delete[] nums;
        return ans;
    }

    static bool powerCompare (const int a, const int b) {
        int step_a = powerValue(a);
        int step_b = powerValue(b);
        if (step_a == step_b)
            return a < b;
        else
            return step_a < step_b;
        
    }

    static int powerValue(int n) {
        int step = 0;
        while (n != 1) {
            if (n % 2 == 0)
                n = n / 2;
            else
                n = 3 * n + 1;
            step ++;
        }
        return step;
    }
};