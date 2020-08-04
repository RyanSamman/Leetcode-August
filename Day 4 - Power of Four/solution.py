class Solution:
	def isPowerOfFour(self, num: int) -> bool:
		return num in [1 << 2*x for x in range(16)]
	
	# Naive solution
	def isPowerOfFour1(self, num: int) -> bool:
		# 16 is log4(2**32) => 32 * log4(2) => 32 * 1/2 => 32 // 2
		for i in map(lambda x: 4 ** x, range(16)): 
			if num < i: break 
			if i == num: return True
		return False

