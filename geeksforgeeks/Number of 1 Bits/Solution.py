class Solution:
	def setBits(self, N):
		# code here
		b = str(bin(N).replace("0b", ""))
		count = 0
		
		
		for i in range(len(b)):
		    if b[i] == "1":
		        count += 1
		
	    return count
