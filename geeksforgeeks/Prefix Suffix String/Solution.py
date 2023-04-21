class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        suffixes = set(s[len(s) - i:] for s in s1 for i in range(1, len(s)))
        prefixes = set(s[:i] for s in s1 for i in range(1, len(s)))
        count = 0
        for s in s2:
            if s in suffixes or s in prefixes:
                count += 1
        return count
