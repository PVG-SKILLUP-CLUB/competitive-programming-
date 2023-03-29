class Solution
{
    public:
    int countSubstring(string s)
    {
        map<int, int> mp; 
        int cur = 0, ans = 0;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] >= 'A' && s[i] <= 'Z') cur++;
            else cur--;
            
            if(cur == 0) ans++;
            ans += mp[cur]++;
        }
        return ans;
    }
};
