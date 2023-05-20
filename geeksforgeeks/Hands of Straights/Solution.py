class Solution:
    def isStraightHand(self,N, groupSize, hand):
        mp = {}
        for i in hand:mp[i] = mp.get(i, 0)+1
        hand.sort()
        
        for card in hand:
            if not mp[card]:continue
            
            for j in range(groupSize):
                curCard = card + j
                if mp.get(curCard, 0) == 0:return False
                mp[curCard] -= 1
        
        return True
