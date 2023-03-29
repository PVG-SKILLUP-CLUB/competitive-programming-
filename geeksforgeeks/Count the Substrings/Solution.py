class Solution:
    def countSubstring(self, s: str) -> int:
        m = {0: 1}
        cnt = 0
        ans = 0
        for c in s:
            cnt += 1 if c.isupper() else -1
            ans += m.get(cnt, 0)
            m[cnt] = m.get(cnt, 0) + 1
        return ans
