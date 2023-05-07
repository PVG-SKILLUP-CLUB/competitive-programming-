class Solution:

        def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

            n = len(obstacles)

            answer = [1] * n

            lis = []

            for i, height in enumerate(obstacles):

                idx = bisect.bisect_right(lis, height)

                if idx == len(lis):lis.append(height)

                else:lis[idx] = height

                answer[i] = idx + 1

            return answer
