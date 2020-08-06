# Prerequisite Question to this Day
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
	def __init__(self):
		self.dict = {}
		
	# Inserts a word into the trie.
	def insert(self, word: str) -> None:
		currNode = self.dict
		for c in word:
			if c not in currNode:
				currNode[c] = {}
			currNode = currNode[c]
		currNode['\0'] = '\0'
		print(self.dict)
		
	# Returns if the word is in the trie.
	def search(self, word: str) -> bool:
		currNode = self.dict
		for char in word:
			if char not in currNode:
				return False
			currNode = currNode[char]
		print(currNode)
		if '\0' in currNode: return True
		return False

	# Returns if there is any word in the trie that starts with the given prefix.
	def startsWith(self, prefix: str) -> bool:
		isStartingWithPrefix = True
		currNode = self.dict
		for c in prefix:
			if c not in currNode:
				isStartingWithPrefix = False
				break
			currNode = currNode[c]
	
		return isStartingWithPrefix
		

if __name__ == "__main__":
	print('\0')
	# Your Trie object will be instantiated and called as such:
	word = "hello"
	prefix = "ab"
	obj = Trie()
	obj.insert('app')
	obj.insert('apple')
	print(obj.dict)
	param_2 = obj.search('apple')
	print(param_2)
	param_3 = obj.startsWith('app')
	print(param_3)

	x = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
	y = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
	