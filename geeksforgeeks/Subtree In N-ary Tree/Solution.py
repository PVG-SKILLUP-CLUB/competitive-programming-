class Solution:
    def duplicateSubtreeNaryTree(self, root):
        
        from collections import Counter
        c = Counter()
        
        def dfs(n):
            nonlocal c
            if not n:
                return "#"
            
            key = "{0} {1}".format(n.key, " ".join(dfs(nxt) for nxt in n.children))
            c[key] += 1
            return key
        
        dfs(root)
        return sum(v > 1 for v in c.values())
