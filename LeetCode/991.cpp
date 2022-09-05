/*
$991. Broken Calculator
*/

class Solution {
public:
    int brokenCalc (int X, int Y) {
        int step = 0;
        while (Y > X) {
            if (Y % 2 == 0) {
                Y /= 2;
                step ++;
            } else {
                Y = Y + 1;
                step ++;
            }
        }
        return step + X - Y;
    }
};