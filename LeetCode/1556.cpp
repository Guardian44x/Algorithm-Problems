/*
$1556. Thousand Separator
*/

class Solution {
public:
    string thousandSeparator(int n) {
        string ans;
        if (n == 0)
            return "0";
        int count = 0;
        int rem = 0;
        while (n > 0) {
            rem = n % 10;
            n = n / 10;
            // cout << (char)('0' + rem)<<endl; 
            ans = (char)('0' + rem) + ans;
            count += 1;
            if (count % 3 == 0 && n > 0)
                ans = '.' + ans;
        }
        return ans;
    }
};