
# Two Pointers Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j, palindrome = 0, len(s) - 1, True
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                palindrome = False
                break

            i += 1
            j -= 1

        return palindrome
