class Solution:

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        dp = {} 

        agekey = sorted(list(set(ages))) 

        hashtable = defaultdict(list) 

        for i in range(len(ages)): 

            hashtable[ages[i]].append(scores[i])

            score = [] 

        for k in agekey:

            score += sorted(hashtable[k]) 

        ages.sort()

        

        def dfs(index):

            if index == len(ages)-1: 

                return score[index] 

            if index in dp:

                return dp[index] 

            dp[index] = score[index] 

            for i in range(index+1,len(ages)):

                if ages[i] > ages[index]: 

                    if score[i] >= score[index]: 

                        dp[index] = max(dp[index],score[index]+dfs(i)) 

                else: 

                    dp[index] = max(dp[index],score[index]+dfs(i)) 

            return dp[index]

        res = 0 

        for k in range(len(ages)): 

            res = max(res,dfs(k)) 

        return res
