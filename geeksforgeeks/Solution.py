class Solution:
      def nearestSmallestTower(self,arr):
        INF = float('inf')
        n = len(arr)
        left, right = [INF]*n, [INF]*n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                left[idx] = i
            stack.append(i)
        
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                right[idx] = i
            stack.append(i)
            
        ans = []
        for i in range(n):
            if left[i] == INF and right[i] == INF:
                ans.append(-1)
            else:
                if abs(left[i]-i) < abs(right[i]-i):
                    ans.append(left[i])
                elif abs(left[i]-i) > abs(right[i]-i):
                    ans.append(right[i])
                elif arr[left[i]] >= arr[right[i]]:
                    ans.append(right[i])
                else:
                    ans.append(left[i])
        return ans
