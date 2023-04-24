class Solution:
    def minSubtreeSumBST(self, target, root):
        def _solve(nd):# sum, isbst, total_nodes, min, max
            nonlocal ans
            if not nd: return 0, True, 0, inf, -inf
            Lsum, Lisbst, Lcnt, Lmin, Lmax = _solve(nd.left)
            Rsum, Risbst, Rcnt, Rmin, Rmax = _solve(nd.right)
            if not Lisbst or not Risbst or nd.data<=Lmax or nd.data>=Rmin: return (0, False, 0, inf, -inf)
            su = Lsum + Rsum + nd.data
            tot = Lcnt + Rcnt + 1
            if su == target:
                ans = min(ans, tot)
            if not nd.left: Lmin = nd.data
            if not nd.right: Rmax = nd.data
            return su, True, tot, Lmin, Rmax
            
        ans = inf
        _solve(root)
        return ans if ans != inf else -1
