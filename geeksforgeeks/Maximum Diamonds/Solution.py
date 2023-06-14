class Solution:
    def maxDiamonds(self, arr, n, k):
        from heapq import heapify, heappop, heappush
        # heapq is a "min heap", to obtain "max heap"
        # we need to negate the elements
        for i in range(n):
            arr[i] *= -1
        heapify(arr)
        diamonds = 0
        for _ in range(k):
            # We negate the "negative minimum value"
            # from the heap to have the maximal one
            max_diamonds = -heappop(arr)
            # and we negate it again before insertion
            heappush(arr, -(max_diamonds // 2))
            diamonds += max_diamonds
        return diamonds
