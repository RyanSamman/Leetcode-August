import re
from time import time

class Solution:
    # My First Solution
    def detectCapitalUse(self, word: str) -> bool:
        c = len([c for c in word if c.isupper()])
        if c == len(word) or c == 0 or c == 1 and word[0].isupper():
            return True
        return False

    # Regex solution
    def sol1(self, word):
        if re.match(r"^([a-z]+|[A-Z][a-z]+|[A-Z]+)$", word): return True
        return False
    
    # Split Regex solution
    def sol2(self, word):
        if re.match(r"^[a-z]+$", word): return True
        if re.match(r"^[A-Z][a-z]+$", word): return True
        if re.match(r"^[A-Z]+$", word): return True
        return False
    
    # Cleaner non-regex solution
    def sol3(self, word: str) -> bool:
        count = len([c for c in word if c.isupper()])
        return any([count == len(word),
                    count == 0,
                    count == 1 and word[0].isupper()])



if __name__ == "__main__":
    sol = Solution()
    startTime = time()
    for i in range(100000):
        assert sol.sol("ABC")
        assert sol.sol("abc")
        assert sol.sol("Abc")
        assert sol.sol("AbC") is False
        assert sol.sol("testingA") is False
    print(time() - startTime)

# Results:
# Manual 0.60s
# Clean  0.64s
# Regex: 0.68s
# Split Regex: 1.2s
# Therefore, Regex is the best option for 