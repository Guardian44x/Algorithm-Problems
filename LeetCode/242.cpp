class Solution {
    public:
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
            return false;
        unordered_map<char, int> mp_s, mp_t;
        for (char c: s)
            mp_s[c]++;
        for (char c: t)
            mp_t[c]++;
        for (int i = 0; i < s.size(); i++)
            if (mp_s[s[i]] != mp_t[s[i]])
                return false;
        return true;
    }
