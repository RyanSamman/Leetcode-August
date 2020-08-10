class Solution:
    def __init__(self):
        self.A = ord('A') # integer representation of A
        self.Z = ord('Z') # integer representation of Z
        self.DIFF = self.Z - self.A + 1 # Number of characers between A and Z inclusive
    
    def charToRange(self, c):
        return ord(c) - (self.A - 1) # Map A to 1, Z to 26
    
    def titleToNumber(self, s: str) -> int:
        return sum(self.DIFF ** i * self.charToRange(c) for i, c in enumerate(s[::-1]))
    
    # Alternatives
    def t2n3(self, s: str) -> int:
        return sum(26 ** i * (ord(c) - 64) for i, c in enumerate(s[::-1]))
    
    def t2n2(self, s):
        return sum(26 ** i * (ord(s[len(s) - i - 1]) - 64) for i in range(len(s)))
    
    def t2n1(self, s):
        return sum(26 ** (i - 1) * (ord(s[-i]) - 64) for i in range(1, len(s) + 1))
    
    def t2n(self, s):
        num = 0
        for i in range(1, len(s) + 1):
            num += 26 ** (i - 1) * (ord(s[-i]) - 64)
        return num