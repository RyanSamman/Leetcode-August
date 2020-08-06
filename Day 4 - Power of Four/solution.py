import time
class Solution:
	# Naive solution
	def isPowerOfFour(self, num: int) -> bool:
		# The size of a normal unsigned integer is 4 bytes, or 32 bits
		# 16 is log4(2**32) = 32 * log4(2) = 32 * 1/2 = 32 // 2 = 16
		for i in map(lambda x: 4 ** x, range(16)): 
			if num < i: break 
			if i == num: return True
		return False

	# Cleaner & Faster solution
	def isPowerOfFour1(self, num: int) -> bool:
		# 1 << x is the equivilent of doing 1 * 2^x
		# This is achieved by shifting the bytes right by 'x' 
		# 1 (...01) becomes 2 (...10) when shifted by 1, 4 (...100) when shifted by 2, 8 (...1000) when shifted by 3 etc.
		# Therefore in 1 << 2*x, you are finding 1 * 2 ^ (2 * x) === (2 * 2) ^ x === 4 ^ x
		return num in (1 << 2*x for x in range(16)) # Calculates all powers of 4 that fits inside an int then checks if num is inside

	# Fastest solution - breaks early and doesn't calculate all powers of 4
	def isPowerOfFour2(self, num: int) -> bool:
		# 16 is log4(2**32) => 32 * log4(2) => 32 * 1/2 => 32 // 2
		for i in (1 << 2*x for x in range(16)): 
			if num < i: break 
			if i == num: return True
		return False


if __name__ == "__main__":
	x = Solution()
	init = time.time()
	for i in range(2 ** 20):
		x.isPowerOfFour2(i)
	print(time.time() - init)