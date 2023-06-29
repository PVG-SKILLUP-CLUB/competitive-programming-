class Solution:
    def is_happy(self, a):
        if a == 1:
            return True
        elif a == 4:
            return False
        else:
            return self.is_happy(sum(int(d)**2 for d in str(a)))

    def nextHappy (self, N):
        while True:
            N += 1
            if self.is_happy(N):
                return N
