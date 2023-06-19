class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        path=[0]
        for i in range(len(gain)):
            path.append(path[i]+gain[i])
        return max(path)
