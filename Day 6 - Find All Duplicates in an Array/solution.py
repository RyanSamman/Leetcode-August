from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums) 
        return [key for key in c.keys() if c[key] == 2]
